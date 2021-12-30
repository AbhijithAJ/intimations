"""                           
    ____      __  _                 __  _                 
   /  _/___  / /_(_)___ ___  ____ _/ /_(_)___  ____  _____
   / // __ \/ __/ / __ `__ \/ __ `/ __/ / __ \/ __ \/ ___/
 _/ // / / / /_/ / / / / / / /_/ / /_/ / /_/ / / / (__  ) 
/___/_/ /_/\__/_/_/ /_/ /_/\__,_/\__/_/\____/_/ /_/____/  
                                                          
'''

intimations 

Basic Beep sound intimations:
    >>> from intimations import *
    >>> beep('success', count=1)

...Push intimations:
    >>> push(title='Process', message='Done Successfully.', icon='success')

...Telegram bot message:
    >>> telegram(botAPI='YOUR_BOT_API', chatID='YOUR_CHATID', title='Process', message='Cloud Process Executed Successfully')



"""
import sys
import os.path, time
from playsound import playsound
from threading import Thread
import urllib.request

if sys.platform == 'win32':
    import ctypes
    from win10toast import ToastNotifier 

def flashIcon(count:int=3, interval:float=1.5):
    '''Flash the icon on windows taskbar'''
    if sys.platform != 'win32':
        raise Exception('Icon flasing is only supported on windows')
    interval = interval if interval > 1.5 else 1.5
    def _run():
        for _ in range(count): # flash the Icon for n number of times with a interval
            ctypes.windll.user32.FlashWindow(ctypes.windll.kernel32.GetConsoleWindow(), True)
            time.sleep(interval)
    Thread(target=_run, args=()).start()

def beep(sound='info', count:int=1, interval:float=3.0):
    '''Plays a sound (mp3/wav). Default sounds 
    info, danger, warning, success'''
    interval = interval if interval > 3.0 else 3.0
    if sound in ['info', 'danger', 'success', 'warning']:  
        sound = f'{os.path.dirname(os.path.abspath(__file__))}/Sounds/{sound}.wav' #get modules path and directory
    sound = os.path.abspath(sound)
    def _run():
        for _ in range(count):#  play the sound for n number of times with a interval
            playsound(sound)
            time.sleep(interval)
    Thread(target=_run, args=()).start()
   
def push(title:str='intimations', message:str='By Abhijith Boppe', duration:float=3, icon=r"sign"):
    '''intimations message takes with an icon.
    Default icons info, danger, warning, success
    '''
    if icon in ['sign','info','danger', 'warning', 'success']:
        icon = f'{os.path.dirname(os.path.abspath(__file__))}/Icons/{icon}.ico'
    icon = os.path.abspath(icon)
    def _run():
        if sys.platform == 'win32': # check for windows platform  
            while 1:
                #windows toast Notifier cant handle multiple notifications at once. 
                try:ToastNotifier().show_toast(title, message, duration=duration, icon_path=icon);break
                except Exception as e: time.sleep(0.3)
        elif sys.platform == 'Darwin': # macos
            try:os.system(f'osascript -e \'display notification "{title}!" with title "{message}"\'')
            except Exception as e: raise Exception(f'command osascript not found. Install it to continue.')
        else: # linux
            try:os.system(f"notify-send -i '{icon}' '{title}' '{message}'")
            except Exception as e: raise Exception(f'command notify-send not found. Install it to continue.')

    Thread(target=_run, args=()).start()

def _getenv(var):
    try:
        return os.environ[var].strip() #get environmental variable values
    except Exception as e:
        raise Exception(f'No BOTAPI/CHATID in the environmental variables. Pass them as arguments insted.')

def telegram(botAPI:'str'=None, chatID:str=None, title:str='intimations', message:str='By Abhijith Boppe'):
    '''Send message to telegram with telegram bot api and it's chat id
    '''
    botAPI = botAPI if botAPI not in [None, '']  else _getenv('BOTAPI') 
    chatID = chatID if chatID not in [None, '']  else _getenv('CHATID')
    title = urllib.parse.quote_plus(title)
    message = urllib.parse.quote_plus(message)
    url_send_message = f"https://api.telegram.org/bot{botAPI}/sendMessage?chat_id={chatID}&text=*{title}*%0A%0A{message}&parse_mode=markdown"
    def _run():
        try: response = urllib.request.urlopen(url_send_message)
        except Exception as e: raise Exception(f'Invalid api request \n-> {url_send_message}')
        if response.getcode() != 200:
            raise Exception(f'Invalid api request  \n-> {url_send_message}')
    Thread(target=_run, args=()).start()
    

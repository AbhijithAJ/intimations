<h1 align="center">
  intimations v1.0
<div align="center">

[![Generic badge](https://img.shields.io/badge/Made_By-ABHIJITH_BOPPE-BLUE.svg)](https://www.linkedin.com/in/abhijith-boppe/)  
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Generic badge](https://img.shields.io/badge/pypi_package-1.1-DARKGREEN.svg)](https://pypi.org/project/intimation/) [![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/AbhijithAJ/intimation/blob/master/LICENSE) [![PayPal](https://img.shields.io/badge/donate-PayPal-blue.svg)](https://www.paypal.me/abhijithboppes) 
</div>


</h1>

 - Cross platform intimations 
 - Sound intimations and Toast/Message intimations
 - Telegram bot intimations/message
 - Flashing Taskbar Icon (for windows platform)
 - Supports Command line

---
## ABOUT

This module makes it easy to get intimations such as a beep sound, push/toast notification, or a telegram bot message during and after the execution of code/process

- Simply popup alerts, warnings, success or any other actions with different icons
- Make a buzzer sound with different sound effects
- Receive a message intimations to your smartphone (via telegram bot).

*Using this module, telegram messages would be received when execution of a process/code is completed on system or a cloud platform.*

**Benefits**

You can focus on other activities till you receive an intimation about your executing code/process.

Interactive icons and sounds which will intimate you about the executing process/code's activity and saves your time and let you enjoy the status of your executing code/process.

## Installation

You can install intimations by running the following command
```
pip install intimations
```

## Command line Usage

**To get a sound intimations**
```
python -m intimations beep --sound success --count 2 --interval 5
```
*sound : 'info', 'danger', 'success', 'warning' or ANY_MP3_FILE_PATH*

**To get a intimations message**
```
python -m intimations push --title 'TITLE OF INTIMATION' --message 'MESSAGE BODY' --icon success
```
*icon : 'info', 'danger', 'success', 'warning' or ANY_ICO_FILE_PATH*

**To get a Telegram bot intimation/Message**
```
python -m intimations telegram --botapi YOUR_TELEGRAM_BOT_API --chatid YOUR_BOT_CHAT_ID --title 'TITLE OF INTIMATION' --message 'MESSAGE BODY'
```

*Follow the video to create telegram botAPI and get chatID*


https://user-images.githubusercontent.com/47808835/146597010-a5e877c2-affa-45c7-a4ae-947839808043.mp4

```
To get chat id, navigate to 'https://api.telegram.org/bot<YOUR_BOT_API>/getUpdates' in your browser.

Replace '<YOUR_BOT_API>' with your bot api token.
```

## Using Telegram message feature effectively

Initially Create a Telegram bot with the name you like and get the botAPI token and chatID as shown in the video.

Create variables BOTAPI and CHATID in your OS environmental variables and assign values to them.

Now, on your terminal, type your command followed by this python module command, as seen in the sample below.

```
ffuf -w /wordlist.txt -u https://target/FUZZ ; python3 -m intimations telegram -t "Title of Process" -m "Successfully executed"
```
You will receive a telegram intimations on your mobile device instantly after your cloud platform has done FUZZING on your target or done with the process.

### Integrating intimations in code

```python
'''
Developed by Abhijith Boppe - linkedin.com/in/abhijith-boppe/
'''
from intimations import *

#get a beep sound
beep(sound='info', count=3, interval=3.0)

#get a push intimation
push('intimation', 'By Abhijith Boppe', duration:int=10, icon=r"sign")

#get an intimation/message to your telegram mobile app
BOT_API = 'YOUR BOT API'
chatID = 'ONE OF YOUR CHAT ID'

telegram(botAPI=BOT_API, chatID=chatID, title='TITLE', message'YOUR MESSAGE')

#Flash icon on taskbar (windows platform only)
flashIcon(count:int=3, interval:float=1.5)
```

### Have a look at Stock icons and sounds

```python
'''
Developed by Abhijith Boppe - linkedin.com/in/abhijith-boppe/
'''
from intimations import *

for type_ in ['info', 'danger', 'warning' , 'success']:
    beep(sound=type_)
    push(title='Testing', message=f'This is {type_} message.',icon=type_)
    time.sleep(3)
```

<br>
<a href="https://www.buymeacoffee.com/abhijithboppe" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-orange.png" alt="Buy Me A Coffee" width="30%"></a>

---
## License & copyright
© Abhijith Boppe, Security analyst

<a href="https://linkedin.com/in/abhijith-boppe" target="_blank">LinkedIn</a>

Licensed under the [MIT License](LICENSE)

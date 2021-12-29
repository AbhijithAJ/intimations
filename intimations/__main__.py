from .intimations import *
import argparse

def _argsFilter(args):
    '''
    Take sub commands and procede accordingly. 
    '''
    if args.command == 'beep':
        beep(args.sound, int(args.count), float(args.interval))
    elif args.command == 'push':
        push(args.title, args.message, float(args.duration), args.icon)
    elif args.command =='telegram':
        telegram(args.botapi, args.chatid, args.title, args.message)
    elif args.command =='flashIcon':
        flashIcon(int(args.count), float(args.interval))

if __name__=="__main__":
    parser = argparse.ArgumentParser(
        prog='intimations', 
        description='''
Description:
    - push/toast notifications with different icons
    - beep sound with different types of sound
    - telegram message (requires your botAPI and ChatID)
  Know more at https://github.com/AbhijithAJ/intimations''',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''\

DEVELOPED BY:
    Abhijith Boppe
    See more at https://bio.link/abhijithboppe
    Support me: https://www.buymeacoffee.com/abhijithboppe

    Thanks for using the module.
         '''
    )
    sub_cmds = parser.add_subparsers(dest='command') #add dest to get sub command when parsing
    
    cmd_beep = sub_cmds.add_parser("beep", help='produce a beep/buzzer sound')  # adding sub command 'beep' 
    cmd_beep.add_argument('-s', "--sound", default='informative', required=False, help='stock sound: informative, danger, success and warning or any .mp3/.wav file"')   # adding arguments to 'beep'  
    cmd_beep.add_argument('-c', "--count", default=1, required=False, help='no.of time to repeat')
    cmd_beep.add_argument('-i', "--interval", default=3.0, required=False, help='time gap between each iteration')

    cmd_push = sub_cmds.add_parser('push', help='send a Push notification')
    cmd_push.add_argument('-t',"--title", default='intimations', required=False, help='Title of the message')
    cmd_push.add_argument('-m',"--message", default='By Abhijith Boppe', required=False, help='Message body')
    cmd_push.add_argument('-d',"--duration", default=3, required=False, help='no.of sec to display the notification')
    cmd_push.add_argument('-i',"--icon", default='sign', required=False, help="stock icons: informative, danger, success and warning or any .ico file")

    cmd_telegram = sub_cmds.add_parser('telegram', help='send a telegram message')
    cmd_telegram.add_argument('-b',"--botapi", required=False, help='API Token of your telegram bot')
    cmd_telegram.add_argument('-c',"--chatid", required=False, help='ID of the chat to which message has to be delivered')
    cmd_telegram.add_argument('-t',"--title", default='intimations', required=False, help='Title of the notification')
    cmd_telegram.add_argument('-m',"--message", default='By Abhijith Boppe', required=False, help='Message body')

    cmd_flashIcon = sub_cmds.add_parser('flashIcon', help='flash windows taskbar icon')
    cmd_flashIcon.add_argument('-c', "--count", default=3, required=False, help='no.of iterations to flash the icon')
    cmd_flashIcon.add_argument('-i', "--interval", default=1.5, required=False, help='time gap between each iteration')

    _argsFilter(parser.parse_args())  


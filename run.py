import os
import sys
import yaml
import urllib.parse
from main import run

# Set path if launch as a .exe or not
if getattr(sys, 'frozen', False):
    rPath = os.path.dirname(sys.executable)
elif __file__:
    rPath = os.path.dirname(__file__)
os.chdir(rPath)

# Launch
print('''
       ________                     
      / ____/ /___ _____________  __
     / /_  / / __ `/ ___/ ___/ / / /
    / __/ / / /_/ (__  |__  ) /_/ / 
   /_/   /_/\__,_/____/____/\__, /  
                           /____/   

      Google Forms Bot v1.2.1
        https://flassy.xyz/\n''')

# Load config
try :
    with open('config.yaml') as configFile:
        config = yaml.load(configFile, Loader=yaml.FullLoader)
except FileNotFoundError:
    input('• [Error] Config file not found, press any key to exit :\n» ')
    sys.exit()
except yaml.parser.ParserError:
    input('• [Error] The url or formData is not valid, press any key to exit :\n» ')
    sys.exit()
url = config['url']
try :
    formData = dict(urllib.parse.parse_qsl(config['formData']))
except AttributeError:
    formData = config['formData']
if 'dlut' in formData: del formData['dlut']

# Proxies
proxies = input('• Do you want to use proxies? [y/n] :\n» ')

pl = []

if proxies == 'y':

    try:
        for line in open('proxylist.txt', 'r'):
            pl.insert(0, line)
        pl = [item.replace('\n', '') for item in pl]
    except FileNotFoundError:
        input('• [Error] Proxies file not found, press any key to exit :\n» ')
        sys.exit()

    if not pl:
        input(
            '\n[WARNING] The proxylist file is empty, to continue without proxies press enter :\n» '
        )
elif(proxies != 'n'):
    sys.exit()

# Number of awnsers
answersMax = int(input('\n• How many answers do you want to send? (0 will send requests indefinitely) :\n» '))

# Number of treads
if not pl:
    threadsNum = int(input('''
  • How many threads do you want to use? :

  ┍━━ WARNING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    Google may block you from sending requests if you send them too quickly
    over a long period of time. Without proxies, the recommended amount of
    threads is 1 or 2. Consider using some proxies to avoid getting blocked.
  ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
  \n» '''))
else:
    threadsNum = int(input('\n• How many threads do you want to use? :\n» '))

#start
print('\n• Starting...')
run(answersMax, threadsNum, url, formData, pl)
input('• Finished sending answers, press any key to exit :\n» ')
sys.exit()

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

# Load config
with open('config.yaml') as configFile:
    config = yaml.load(configFile, Loader=yaml.FullLoader)
url = config['url']
try:
    formData = dict(urllib.parse.parse_qsl(config['formData']))
except:
    formData = config['formData']

# Run
print('''
       ________                     
      / ____/ /___ _____________  __
     / /_  / / __ `/ ___/ ___/ / / /
    / __/ / / /_/ (__  |__  ) /_/ / 
   /_/   /_/\__,_/____/____/\__, /  
                           /____/   

      Google Forms Bot v1.1.1
        https://flassy.xyz/\n''')

proxies = input('• Do you want to use proxies? [y/n] :\n» ')
if proxies == 'y':

    pl = []
    pf = open('proxylist.txt', 'r')

    for line in pf:
        pl.insert(0, line)
    pl = [item.replace('\n', '') for item in pl]

    if not pl:
        input(
            '\n[WARNING] The proxylist file is empty, to continue without proxies press enter :\n» '
        )

elif proxies == 'n':
    pl = []
else:
    quit()

answersMAx = int(
    input(
        '\n• How many answers do you want to send? (0 will send requests indefinitely) :\n» '
    ))

if not pl:
    threadsNum = int(
        input('''
  • How many threads do you want to use? :

  ┍━━ WARNING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    Google may block you from sending requests if you send them too quickly
    over a long period of time. Without proxies, the recommended amount of
    threads is 1 or 2. Consider using some proxies to avoid getting blocked.
  ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
  \n» '''))
else:
    threadsNum = int(input('\n• How many threads do you want to use? :\n» '))

print('\n• Starting...')

run(answersMAx, threadsNum, url, formData, pl)
input('• Finished sending answers, press enter to exit :\n» ')
quit()
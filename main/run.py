import os, configparser, ast

from pathlib import Path
ePath = Path(os.path.realpath(__file__)).parents[1]

config = configparser.ConfigParser()
config.read(ePath / 'config.ini')
url = config.get('DEFAULT', 'url')
formData = ast.literal_eval(config.get('DEFAULT', 'formData'))

print ('''
       ________                     
      / ____/ /___ _____________  __
     / /_  / / __ `/ ___/ ___/ / / /
    / __/ / / /_/ (__  |__  ) /_/ / 
   /_/   /_/\__,_/____/____/\__, /  
                           /____/   

      Google Forms Bot v1.1.0
        https://flassy.xyz/\n''')

proxies = input('• Do you want to use proxies? [y/n] :\n» ')
if proxies == 'y':
  i = 0
  pl=[]
  
  pf_size = os.stat(ePath / 'proxylist.txt').st_size
  if pf_size == 0:
    input('\n• No proxies were found in the file, press enter to exit :\n» ')
    quit()
  else:
    pf = open(ePath / 'proxylist.txt', 'r')
    
    for line in pf:
      pl.insert(0, line)
      i += 1
    pl = [item.replace('\n', '') for item in pl]
elif proxies == 'n':
  pl = ['00.00.00.00:0000']
else:
  quit()

awnsersNum = int(input('\n• How many awnser do you want to send? (0 will send requests indefinitely) :\n» '))

if proxies == 'n':
  threadsNum = int(input('''
  • How many threads do you want to use? :

  ┍━━ WARNING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
    Google may block you from sending requests if you send them too quickly
    over an extended period of time. In that case, the recommended number of
    threads is 1 or 2. Consider using some proxies to avoid getting blocked.
  ┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
  \n» '''))
else:
  threadsNum = int(input('\n• How many threads do you want to use? :\n» '))

print('\n• Starting...')

from main import run
run(awnsersNum, threadsNum, url, formData, pl)
input('• Finished sending awnsers, press enter to exit :\n» ')
quit()
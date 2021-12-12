import os, configparser, ast

from pathlib import Path
cPath = Path(os.path.realpath(__file__)).parents[1]

config = configparser.ConfigParser()
config.read(cPath / 'config.ini')
url = config.get('DEFAULT', 'url')
formData = ast.literal_eval(config.get('DEFAULT', 'formData'))

print ('''
       ________                     
      / ____/ /___ _____________  __
     / /_  / / __ `/ ___/ ___/ / / /
    / __/ / / /_/ (__  |__  ) /_/ / 
   /_/   /_/\__,_/____/____/\__, /  
                           /____/   

      Google Forms Bot v1.0.0
        https://flassy.xyz/\n''')

awnsersNum = int(input('\n• How many awnser do you want to send? (0 will send requests indefinitely) :\n» '))

threadsNum = int(input('''
• How many threads do you want to use? :

┍━━ WARNING ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
  Google may block temporarily your requests if you send awnsers too quickly 
  1 thread: no chance of getting blocked                                     
  2 threads: some chance of getting blocked afer a while                     
  3+ threads: high chance of getting blocked afer a while                                
┕━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┙
\n» '''))
print('\n• Starting...')

from main import run
run(awnsersNum, threadsNum, url, formData)
input('• Finished sending awnsers, press enter to exit')
quit()
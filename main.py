import requests
import threading
import random
import time
from datetime import timedelta

awnsersSent = 0
nPrint = 0
startTime = 0

# Run the script (Multithreaded)
def run(answersMax, threadsNum, url, formData, proxyList):
    global startTime
    startTime = time.time()
    
    threads = [threading.Thread(target=sendRequests, args=(answersMax, url, formData, proxyList,), daemon=True) for t in range(threadsNum)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return()

# Send requests
def sendRequests(answersMax, url, formData, proxyList):
    global awnsersSent
    while answersMax == 0 or awnsersSent < answersMax:
        awnsersSent += 1
        
        # With proxies
        if proxyList:
            rand = random.randrange(len(proxyList))
            proxy = proxyList[rand]
            
            # Try with a proxy
            try: requests.get(url, proxies={'http': 'http://'+proxy, 'https': 'http://'+proxy, }, allow_redirects=False, data=formData, timeout=5)
                
            # If a proxy is not working (Delete it from proxyList)
            except: 
                try:
                    if (proxyList and proxy == proxyList[rand]):
                        del proxyList[rand]
                        print(f'  [Unable to connect to {proxy}]' + '   ' * 30, end='\r\n')
                except:
                    pass
                requests.post(url, allow_redirects=False, data=formData)
                
        # Without proxies
        else:
            requests.post(url, allow_redirects=False, data=formData)
        printAwnser(answersMax)
    return()

#Print total awnsers sent
def printAwnser(answersMax):
    global nPrint
    global startTime
    elapsedTime = str(timedelta(seconds=round(time.time() - startTime)))
    nPrint += 1
    if (answersMax == 0): 
        print(f'  {nPrint} answers sent | Time Elapsed:{elapsedTime}', end='\r')
    else:
        percent = (nPrint / answersMax) * 50
        bar = '█' * int(percent) + '░' * (50 - int(percent))
        print(f'  {bar} Progress: {nPrint}/{answersMax} | Time Elapsed: {elapsedTime}', end='\r')
    return()

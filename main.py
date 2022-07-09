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
        
        # Get proxies
        if (proxyList):
            rand = random.randrange(len(proxyList))
            rProxy = proxyList[rand]
            proxy = {'http': 'http://'+rProxy, 'https': 'https://'+rProxy, }
        else:
            proxy = {'http': None,'https': None,}
            
        try:
            requests.post(url, proxies=proxy, allow_redirects=False, data=formData, timeout=5)    
        except:
            
            try:
                if (proxyList and rProxy == proxyList[rand]):
                    print(f'   [Unable to connect to {rProxy}]' + '   ' * 30, end='\r\n')
                    del proxyList[rand]
            except:
                pass
            
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
        print(f'   {nPrint} answers sent | Time Elapsed:{elapsedTime}', end='\r')
    else:
        percent = (nPrint / answersMax) * 50
        bar = '█' * int(percent) + '░' * (50 - int(percent))
        print(f'   {bar} Progress: {nPrint}/{answersMax} | Time Elapsed: {elapsedTime}', end='\r')
    return()

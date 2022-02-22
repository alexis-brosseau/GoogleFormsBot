import requests
import threading
import random

awnsersSent = 0
nPrint = 0

# Run the script (Multithreaded)
def run(answersMax, threadsNum, url, formData, proxyList):
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
            try:
                requests.get(url, proxies={'http': 'http://'+proxy, 'https': 'http://'+proxy, }, allow_redirects=False, data=formData, timeout=5)
                printAwnser()
                
            # If a proxy is not working (Delete it from proxyList)
            except:
                if proxyList:
                    del proxyList[rand]
                requests.post(url, allow_redirects=False, data=formData)
                print('[Unable to connect to %s]' %(proxy))
                printAwnser()
        # Without proxies
        else:
            requests.post(url, allow_redirects=False, data=formData)
            printAwnser()
    return()

#Print total awnsers sent
def printAwnser():
    global nPrint
    nPrint += 1
    print('  %s answers sent' % (nPrint))
    return()

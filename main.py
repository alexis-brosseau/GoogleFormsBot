import requests
import threading
import random

awnsersSent = 0
nPrint = 0

# Main loop
def check(answersMax, url, formData, proxyList):
    global awnsersSent
    while answersMax == 0 or awnsersSent < answersMax:
        sendRequests(url, formData, proxyList)
    return()

# Send requests
def sendRequests(url, formData, proxyList):
    global awnsersSent
    global nPrint
    with threading.Lock():
        awnsersSent += 1
    
    # With proxies
    if proxyList:
        rand = random.randrange(len(proxyList))
        proxy = proxyList[rand]
        
        # Try with a proxy
        try:
            requests.get(url, proxies={
                         'http': 'http://'+proxy, 'https': 'http://'+proxy, }, allow_redirects=False, data=formData)
            nPrint += 1
            print('  %s answers sent' % (nPrint))
            
        # If a proxy is not working (Delete it from proxyList)
        except:
            if proxyList:
                del proxyList[rand]
            requests.post(url, allow_redirects=False, data=formData)
            nPrint += 1
            print('  %s answers sent \n [Unable to connect to %s]' % (nPrint, proxy))
    # Without proxies
    else:
        requests.post(url, allow_redirects=False, data=formData)
        nPrint += 1
        print('  %s answers sent' % (nPrint))
    return()

# Multithreading
def run(answersMax, threadsNum, url, formData, proxyList):
    threads = [threading.Thread(target=check, args=(
        answersMax, url, formData, proxyList,), daemon=True) for t in range(threadsNum)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return()
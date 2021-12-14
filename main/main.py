import requests, threading, os, random

from pathlib import Path
cPath = Path(os.path.realpath(__file__))
ePath = Path(os.path.realpath(__file__)).parents[1]

n = 0
nPrint = 0

def check(answersNum, url, formData, proxyList):
    global n
    
    while answersNum == 0:
        sendRequests(url, formData, proxyList)
    else:
        while n < answersNum:
            sendRequests(url, formData, proxyList)
    with threading.Lock():
        n += 1
    return()

def sendRequests(url, formData, proxyList):
    global n
    global nPrint
    proxy = proxyList[random.randrange(len(proxyList))]
    
    with threading.Lock():
        n += 1
    if proxyList[0] != 'null':
        proxy = proxyList[random.randrange(len(proxyList))]
        try:
            requests.get(url, proxies={'http': 'http://'+proxy, 'https': 'http://'+proxy,}, allow_redirects=False, data=formData,)
            nPrint += 1
            print('  %s answers sent' %(nPrint))
        except:
            requests.post(url, allow_redirects=False, data=formData)
            nPrint += 1
            print('  %s answers sent [Sended without proxy because %s failed to connect]' %(nPrint, proxy))
    else:
        requests.post(url, allow_redirects=False, data=formData)
        nPrint += 1
        print('  %s answers sent' %(nPrint))
    return()

def run(answersNum, threadsNum, url, formData, proxyList):
    threads = [threading.Thread(target=check, args=(answersNum, url, formData, proxyList,), daemon = True) for t in range(threadsNum)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
import requests, threading, os, random

from pathlib import Path
cPath = Path(os.path.realpath(__file__))
ePath = Path(os.path.realpath(__file__)).parents[1]

n = 0
nPrint = 0

def check(awnsersNum, url, formData, proxyList):
    global n
    
    while awnsersNum == 0:
        sendRequests(url, formData, proxyList)
    else:
        while n < awnsersNum:
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

    try:
        requests.get(url, proxies={'http': 'http://'+proxy, 'https': 'http://'+proxy,}, allow_redirects=False, data=formData,)
        nPrint += 1
        print('  %s awnsers sent' %(nPrint))
    except:
        requests.post(url, allow_redirects=False, data=formData)
        nPrint += 1
        if proxy == '00.00.00.00:0000':
            print('  %s awnsers sent' %(nPrint))
        else:
            print('  %s awnsers sent [Sended without proxy because %s failed]' %(nPrint, proxy))
    return()

def run(awnsersNum, threadsNum, url, formData, proxyList):
    threads = [threading.Thread(target=check, args=(awnsersNum, url, formData, proxyList,), daemon = True) for t in range(threadsNum)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
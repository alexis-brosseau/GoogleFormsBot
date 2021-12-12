import requests, threading

n = 0
threadLock = threading.Lock()

def check(awnsersNum, url, formData):
    global n
    
    while awnsersNum == 0:
        sendRequests(url, formData)
    else:
        while n < awnsersNum:
            sendRequests(url, formData)
    return()

def sendRequests(url, formData):
    global n
    
    with threadLock:
        n += 1
        print('  %d awnsers sent' %(n))
    requests.post(url, allow_redirects=False, data=formData)

def run(awnsersNum, threadsNum, url, formData):
    threads = [threading.Thread(target=check, args=(awnsersNum, url, formData,), daemon = True) for t in range(threadsNum)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
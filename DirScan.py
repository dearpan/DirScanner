import time
import threading
import requests
import argparse

argapr = argparse.ArgumentParser(description='Help to DirScan.py')
argapr.add_argument('-u','--url',help="Site target scan Url.",default="https://www.baidu.com")
argapr.add_argument('-t','--thread',help="Site scan thread number.",default=10)
args = argapr.parse_args()
print(args)

lock = threading.Lock()
File_open = open("./PHP.txt","r+")
GetUrl = args.url
ThreadNum = args.thread

def job(self):
    lock.acquire()
    time.sleep(0.2)
    for content in File_open:
        content = File_open.readline()
        ScanUrl = GetUrl + content
        UrlRquest = requests.get(ScanUrl,timeout=5)
        if(UrlRquest.status_code == 200):
            print("[+] " + ScanUrl)
    lock.release()

# 主线程
def main():
    print('''
       _____  .__                       .__
      /  _  \ |  | _____    ____   ____ |__|
     /  /_\  \|  | \__  \  /    \ /    \|  |
    /    |    \  |__/ __ \|   |  \   |  \  |
    \____|__  /____(____  /___|  /___|  /__|
            \/          \/     \/     \/
    ''')
    for i in range(int(ThreadNum)):
        Th = threading.Thread(target=job, args=(i,))
        Th.start()
        Th.join()
    print('Scan is done...')

if __name__ == '__main__':
    main()


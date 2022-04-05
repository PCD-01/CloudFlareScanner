from concurrent.futures import ThreadPoolExecutor
import threading
import time
import requests
import ipaddress

ip1 = 104
ip2 = 21
ip3 = 225
ip4 = 1

def scanip(url):
    #requests.packages.urllib3.disable_warnings()
    r = requests.get(url,headers={'Host':'furrycloud.cf'}, timeout=1)
    if("68621db880e735ba6ef49e04bb8b1f9c" in r.text):
        print("[+] "+url+" 反代CloudFlare.jpg")
        with open("ScanedIP.txt","a") as f:
            f.write(url)
            f.write("\n")

def getip(a):
    scanip(str(a))

def get_thread():
    time.sleep(3)
    while(1):
        if(threading.active_count()!=2):
            print("当前线程数: "+str(threading.active_count()-1))
        else:
            print("当前线程数: 1")
            break
        time.sleep(1)

def main():
    network = ipaddress.ip_network('0.0.0.0/0')
    threads = input("需要的线程数:")
    need = int(threads)
    with ThreadPoolExecutor(need) as tpool:
        tpool.submit(get_thread,)
        for ip in network:
            tpool.submit(getip,ip)

if __name__ == '__main__':
    main()
import threading
import time
import requests

ip1 = 1
ip2 = 1
ip3 = 1
ip4 = 1

def scanip(url):
    try:
        r = requests.get(url,headers={'Host':'furrycloud.cf'},verify=False)
        if("1145141919810" in r.text):
            with open("test.txt","a") as f:
                f.write(url)
    except:
        pass

def getip():
    global ip1
    global ip2
    global ip3
    global ip4
    ip4+=1
    if(ip4>255):
        ip4=1
        ip3+=1
        if(ip3>255):
            ip3=1
            ip2+=1
            if(ip2>255):
                ip2=1
                ip1+=1
                if(ip1>255):
                    exit()
    scanip(str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4))

def get_thread():
    while(1):
        print(threading.active_count()) # 显示当前激活的线程数
        print(threading.enumerate()) # 显示当前激活的线程
        print(threading.current_thread()) # 当前运行的线程 
        time.sleep(30)

def main():
    threads = input("需要的线程数:")
    need = int(threads)
    thread = threading.Thread(target=get_thread,)
    thread.start() # 开始该线程
    while(1):
        if(threading.active_count()<=need):
            thread = threading.Thread(target=getip,)
            thread.start() # 开始该线程
        else:
            time.sleep(5)

if __name__ == '__main__':
    main()
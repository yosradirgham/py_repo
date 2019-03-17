import platform
import time
import pandas
from datetime import datetime as dt

websites=["www.asos.fr","www.asos.com","www.facebook.com","www.amazon.*"]
redirect = "127.0.0.1"

def get__os__name():
    os = platform.system()
    if os=="Linux" or os=="Darwin":
        return "/etc/hosts"
    elif os==Windows:
        return "C:\Windows\System32\drivers\etc\hosts"


def read__hosts__file():
    arr = []
    with open(get__os__name(),"r") as f:# r for reading, w for writing, r+ for reading and writing
        f.readline()
        for line in f:
            if line[0]=='#' :
                pass
            else:
                arr.append(line)
    return arr


def alter__hosts__file(my_list):
    with open(get__os__name(),"a") as f:
        for website in websites:
            if website+'\n' in my_list or "127.0.0.1 "+website+"\n" in my_list:
                continue
            else:
                f.write(redirect+" "+website+"\n")


def overwrite__hosts__file():
    with open(get__os__name(),"r+") as f:
        lines_list = f.readlines()
        f.seek(0)
        for line in lines_list:
            if not any(website in line for website in websites):
                f.write(line)
        f.truncate()


def block__websites():
    while True:
        if dt(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,8) < dt.now() <dt(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,16)  :
            hosts_data = read__hosts__file()
            alter__hosts__file(hosts_data)
            print('working hours')
            break
        else:
            overwrite__hosts__file()
            print('fun time')
            break

hosts_path = get__os__name()
block__websites()

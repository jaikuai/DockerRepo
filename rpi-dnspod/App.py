# coding:utf8
import json
import urllib.request
import urllib
import threading
import os
import ssl

## 设定域名token和二级域名
token     = os.environ.get("TOKEN")
domain    = os.environ.get("DOMAIN")
name      = os.environ.get("NAME")
wait_time = os.environ.get("TIME")


def do():
    ssl._create_default_https_context = ssl._create_unverified_context
    ## Get MyIP
    s = urllib.request.urlopen("http://pv.sohu.com/cityjson").read().decode('gbk')
    ip_data = json.loads(str(s)[19:-1])
    
    ## Get Domain Info
    param = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain})
    data = urllib.request.urlopen("https://dnsapi.cn/Record.List", param.encode('ascii')).read().decode('UTF-8')
    jdata = json.loads(data)

    record_id = ""
    record_ip = ""
    for obj in jdata["records"]:
        if obj["name"] == name:
            record_id = obj["id"]
            record_ip = obj["value"]
            break
    ## 判断是否更新
    if ip_data["cip"] == "":
        print("Not get IP!")
        pass
    elif record_ip == ip_data["cip"]:
        pass
    elif record_id != "":
        params = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain, "record_id": record_id,"sub_domain": name, "record_type": "A", "record_line": "默认", "value": ip_data["cip"]})
        data = urllib.request.urlopen("https://dnsapi.cn/Record.Modify", params.encode('ascii')).read().decode('UTF-8')
        print(data)
        if int(data["status"]["code"]) == 1 :
            print("Update IP:" + ip_data["cip"])
        else:
            print(data["status"]["message"])

## 定时任务
timer = threading.Timer(int(wait_time), do)
timer.start()

# coding=utf-8
import json
import time
import urllib.request
import urllib
import threading
import os
import ssl
import json

## 设定域名token和二级域名
token     = os.environ.get("TOKEN")
domain    = os.environ.get("DOMAIN")
name      = os.environ.get("NAME")
wait_time = os.environ.get("TIME")


def do():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        ## Get MyIP
        s = urllib.request.urlopen("http://pv.sohu.com/cityjson").read().decode('gbk')
        ip_data = json.loads(str(s)[19:-1])
    except Exception as e:
        print('%s 获取本机IP异常' % now)
        return
    
    ## Get Domain Info
    param = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain})
    data = urllib.request.urlopen("https://dnsapi.cn/Record.List", param.encode('ascii')).read().decode('UTF-8')
    jdata = json.loads(data)

    record_id = ""
    record_ip = ""
    for obj in jdata["records"]:
        if obj["name"] == name and obj['status'] == 'enable' and obj['type'] == 'A':
            record_id = obj["id"]
            record_ip = obj["value"]
            break
    ## 判断是否更新
    if record_ip == ip_data["cip"]:
        print("%s IP相同 %s = %s，跳过" % (now, record_ip,ip_data["cip"]))
        pass
    else:
        params = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain, "record_id": record_id,"sub_domain": name, "record_type": "A", "record_line": "默认", "value": ip_data["cip"]})
        data = urllib.request.urlopen("https://dnsapi.cn/Record.Modify", params.encode('ascii')).read().decode('UTF-8')
        res = json.loads(data)
        if res["status"]["code"] == "1" :
            print("%s Update IP: %s" % (now, ip_data["cip"]))
        else:
            print('%s %s' % (now, res["status"]["message"]))

## 定时任务
timer = threading.Timer(int(wait_time), do)
timer.start()

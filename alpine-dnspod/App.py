# coding=utf-8
import json
import os
import ssl
import threading
import time
import traceback
import urllib
import urllib.request

import requests

## 设定域名token和二级域名
token = os.environ.get("TOKEN", "84020,5b759d903a6975e71fb9d2982d343c24")
domain = os.environ.get("DOMAIN", "it5000.com")
name = os.environ.get("NAME", "rpi")
wait_time = os.environ.get("TIME", 10)


def dingding_talk(text):
    headers = {'Content-Type': 'application/json'}
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c37e089ee476172edf48b9c95e14e77e44e5ab6dae7ef06fadf04bed963442f1'
    data = {
        "msgtype": "text",
        "text": {
            "content": '[RPI]:' + text + '\n'
        },
        "at": {
            "isAtAll": False
        }
    }
    requests.post(url=webhook, data=json.dumps(data), headers=headers)


def do():
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    ssl._create_default_https_context = ssl._create_unverified_context
    try:
        ip = urllib.request.urlopen("https://ipv4.icanhazip.com", timeout=10).read().decode('gbk')
    except Exception as e:
        print('%s 获取本机IP异常' % now)
        dingding_talk('%s 获取本机IP异常' % now)
        return

    try:
        ## Get Domain Info
        param = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain})
        data = urllib.request.urlopen("https://dnsapi.cn/Record.List", timeout=10).read().decode('UTF-8')
        jdata = json.loads(data)

        record_id = ""
        record_ip = ""
        for obj in jdata["records"]:
            if obj["name"] == name and obj['status'] == 'enable' and obj['type'] == 'A':
                record_id = obj["id"]
                record_ip = obj["value"]
                break
        ## 判断是否更新
        if "" == record_ip:
            print("%s 获取当前IP报错，跳过: {}" % (now, name))
        elif ip is None or record_ip.strip() == ip.strip():
            print("%s IP相同 %s = %s 跳过" % (now, record_ip, ip.strip()))
            pass
        else:
            params = urllib.parse.urlencode({"login_token": token, "format": "json", "domain": domain, "record_id": record_id,"sub_domain": name, "record_type": "A", "record_line": "默认", "value": ip})
            data = urllib.request.urlopen("https://dnsapi.cn/Record.Modify", timeout=10).read().decode('UTF-8')
            res = json.loads(data)
            if res["status"]["code"] == "1":
                print("%s Update IP: %s -> %s" % (now, record_ip, ip))
                dingding_talk("%s Update IP: %s -> %s" % (now, record_ip, ip))
            else:
                print('%s %s' % (now, res["status"]["message"]))
    except Exception as e:
        print('%s 获取域名IP或更新时报错' % now)
        dingding_talk("%s 获取域名IP或更新时报错" % now)
        traceback.print_exc()
        return


## 定时任务
timer = threading.Timer(int(wait_time), do)
timer.start()

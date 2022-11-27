FROM alpine

ENV TZ="Asia/Shanghai" TOKEN="" DOMAIN="" NAME="" TIME="300"

# Install python3
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories &&  \ 
    apk add --update && apk add tzdata python3 py3-requests && rm -rf /var/cache/apk/* 

ADD App.py /home/


CMD ["/bin/sh","-c","/usr/bin/python3 /home/App.py"]

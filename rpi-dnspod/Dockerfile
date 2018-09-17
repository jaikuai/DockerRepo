FROM hypriot/rpi-alpine-scratch

ENV TZ="Asia/Shanghai" TOKEN="" DOMAIN="" NAME="" TIME="300"

# Install python3
RUN apk add --update && apk add python3 && rm -rf /var/cache/apk/* 

ADD App.py /home/


CMD ["/bin/sh","-c","/usr/bin/python3 /home/App.py"]

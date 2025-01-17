FROM privateport/alpine-rpi:3.3

RUN apk add --update && apk add python3 redis tzdata && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" 
COPY ./crysadm /crysadm
COPY ./run.sh /run.sh

RUN chmod a+x /run.sh && pip3 install redis && pip3 install requests && pip3 install flask && pip3 install flask-mail

CMD ["/run.sh"]
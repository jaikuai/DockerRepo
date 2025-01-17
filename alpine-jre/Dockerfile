FROM java:8u111-alpine

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App

RUN echo -e "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/main\n\
https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/community" > /etc/apk/repositories

ADD glowroot /home/glowroot/
ADD start.sh /home/

RUN apk --update add tzdata curl bash ttf-dejavu && rm -rf /var/cache/apk/* && chmod a+x /home/start.sh

EXPOSE 8082

CMD ["/home/start.sh"]
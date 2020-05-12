FROM rpi.it5000.com:5000/java:8-jre-alpine

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App

RUN echo -e "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/main\n\
https://mirror.tuna.tsinghua.edu.cn/alpine/v3.4/community" > /etc/apk/repositories
RUN apk --update add tzdata curl bash ttf-dejavu && rm -rf /var/cache/apk/*

CMD ["/bin/sh","-c","/usr/bin/java -jar /home/App.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}"]
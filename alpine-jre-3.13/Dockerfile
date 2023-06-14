FROM alpine:3.13

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && apk --update add tzdata curl openjdk8-jre && rm -rf /var/cache/apk/*

CMD ["/bin/sh","-c","/usr/bin/java -jar /home/App.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}"]
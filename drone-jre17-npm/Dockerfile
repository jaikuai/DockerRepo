FROM alpine:3.15

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App

RUN echo -e "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.15/main\n\
https://mirror.tuna.tsinghua.edu.cn/alpine/v3.15/community" > /etc/apk/repositories
RUN apk --update add tzdata curl bash ttf-dejavu openjdk17 openjdk17-jdk maven npm && rm -rf /var/cache/apk/*

WORKDIR /home

ADD ./settings.xml /usr/share/maven/conf/
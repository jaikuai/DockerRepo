FROM alpine:3.17

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App

RUN echo -e "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.17/main\n\
https://mirror.tuna.tsinghua.edu.cn/alpine/v3.17/community" > /etc/apk/repositories
RUN apk --update add tzdata curl bash ttf-dejavu openjdk17-jre openjdk17-jre-headless && rm -rf /var/cache/apk/*

WORKDIR /home

EXPOSE 8082

CMD ["/bin/sh","-c","/usr/bin/java -jar /home/${PRO_NAME}.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}"]
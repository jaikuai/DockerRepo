FROM alpine:3.13

ENV TZ="Asia/Shanghai" 

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk --update add tzdata && rm -rf /var/cache/apk/*
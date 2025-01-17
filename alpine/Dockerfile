FROM alpine

WORKDIR /home

COPY simhei.ttf /usr/share/fonts/simhei.ttf

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk --update --no-cache add tzdata ttf-dejavu fontconfig
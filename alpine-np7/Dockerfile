FROM alpine:3.11

COPY files/ /
 
RUN cd / && \
    sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories && \
    apk update  && \
    apk add build-base curl shadow openssh bash libxml2-dev openssl-dev libjpeg-turbo-dev libpng-dev libxpm-dev freetype-dev gd-dev gettext-dev libmcrypt-dev binutils && \
    addgroup www  && \
    adduser -G www -D -s /sbin/nologin www  && \
    apk add nginx && \
    apk add php7 php7-fpm php7-opcache php7-curl php7-gd php7-mbstring php7-mysqli php7-json php7-simplexml php7-bcmath php7-mcrypt php7-redis php7-pdo php7-pdo_mysql redis  && \
    apk del build-base shadow binutils && \
    rm -rf  /var/cache/apk/* && \
    chmod +x /run.sh

EXPOSE 80

VOLUME ["/wwwroot"]  

CMD ["/run.sh"]
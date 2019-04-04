FROM alpine:3.3

# Install Nginx Php
RUN apk add --update && apk add tzdata nginx php-openssl openssl php-common php-mysql php-json php-gd php-pdo php-fpm php-pdo_mysql php-mysqli php-ctype php-curl curl php-sqlite3 php-pdo_sqlite && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" TERM=linux

ADD files/ /

RUN chmod +x /run.sh && mkdir -p /run/nginx/

EXPOSE 80

VOLUME ["/data"]  

CMD ["/run.sh"]
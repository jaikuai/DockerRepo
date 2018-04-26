FROM hypriot/rpi-alpine:3.6

# Install Nginx Php
RUN apk add --update && apk add tzdata nginx php5-common php5-mysql php5-json php5-gd php5-pdo php5-fpm php5-pdo_mysql php5-mysqli php5-ctype php5-curl curl && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" TERM=linux

ADD data /
ADD etc /
ADD run.sh /

RUN chmod +x /run.sh && mkdir -p /run/nginx/

CMD ["/run.sh"]

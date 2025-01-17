FROM rpi.it5000.com:5000/jaikuai/alpine-np7:v2

ENV PRO_NAME=mall PRO_ENV=dev TZ="Asia/Shanghai"

ADD default.conf /etc/nginx/conf.d/
ADD ./php.ini /etc/php7/

WORKDIR /wwwroot


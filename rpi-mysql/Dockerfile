FROM hypriot/rpi-alpine-scratch

# Install MySQL
RUN apk add --update && apk add tzdata mysql && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" TERM=linux MYSQL_ROOT_PASSWORD=123456

ADD etc /
ADD run.sh /

RUN mkdir -p /run/mysqld && chmod 777 /run/mysqld && chmod +x /run.sh && mkdir -p /etc/mysql/conf.d/ && chmod 644 /etc/mysql/my.cnf

CMD ["/run.sh"]

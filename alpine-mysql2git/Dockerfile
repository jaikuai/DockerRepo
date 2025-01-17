FROM alpine:3.3

ENV TZ="Asia/Shanghai" GIT_URL="" MYSQL_PASSWORD="" FILE_PATH=""

# Install subversion
RUN apk add --update && apk add tzdata git mysql-client && rm -rf /var/cache/apk/* && git config --global user.name "Bridge" && git config --global user.email "jaikuai@163.com"

ADD start.sh /home/start.sh

RUN chmod a+x /home/start.sh

CMD ["/home/start.sh"]
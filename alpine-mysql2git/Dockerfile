FROM alpine:3.3

ENV TZ="Asia/Shanghai" GIT_URL="/jaikuai/backup.git" GIT_USER="jaikuai" GIT_PASS="" MYSQL_PASSWORD="" MY_DIR="data"

# Install subversion
RUN apk add --update && apk add tzdata git mysql-client && rm -rf /var/cache/apk/* && git config --global user.name "Bridge" && git config --global user.email "jaikuai@163.com" && mkdir -p $MY_DIR

ADD start.sh /home/start.sh

RUN chmod a+x /home/start.sh

CMD ["/home/start.sh"]
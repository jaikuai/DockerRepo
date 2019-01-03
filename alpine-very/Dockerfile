FROM alpine

WORKDIR /home

# Install
RUN apk add --update && apk add tzdata && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" ADR="http://127.0.0.1:8886"

RUN wget http://releases.verysync.com/releases/v0.15.14/verysync-linux-amd64-v0.15.14.tar.gz \ 
    && tar -xvzf verysync-linux-amd64-v0.15.14.tar.gz \
    && rm -f verysync-linux-amd64-v0.15.14.tar.gz

EXPOSE 8886

CMD ["/bin/sh","-c","/home/verysync-linux-amd64-v0.15.14/verysync -gui-address $ADR"]
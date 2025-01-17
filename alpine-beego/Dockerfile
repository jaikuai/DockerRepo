FROM golang:alpine

RUN apk add --update && apk add git && rm -rf /var/cache/apk/* 

#Install beego & bee

RUN go get -u -v github.com/astaxie/beego
RUN go get -u -v github.com/beego/bee
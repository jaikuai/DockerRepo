FROM 102010cncger/goproxy

ENV TZ="Asia/Shanghai" PORT_CLIENT=80

ADD proxy.crt /
ADD proxy.key /

EXPOSE 8080 18080

CMD ["/bin/sh","-c","/proxy bridge -p :8080 -C proxy.crt -K proxy.key --daemon && /proxy server -r :18080@:${PORT_CLIENT} -P 127.0.0.1:8080 -C proxy.crt -K proxy.key"]

## openssl req -new -x509 -newkey rsa:4096 -keyout proxy.key -out proxy.crt

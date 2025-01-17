FROM alpine:3.3

# Install Nginx
RUN apk add --update && apk add tzdata nginx && rm -rf /var/cache/apk/*

ENV TZ="Asia/Shanghai" TERM=linux

COPY default.conf /etc/nginx/conf.d/
COPY nginx.conf /etc/nginx/
COPY cert /home/cert/
COPY reload.sh /home/
COPY start.sh /home/
RUN echo '*/1 * * * * /home/reload.sh'>> /var/spool/cron/crontabs/root && chmod +x /home/start.sh && chmod a+x /home/reload.sh && mkdir -p /run/nginx/

EXPOSE 80 443

CMD ["/home/start.sh"]
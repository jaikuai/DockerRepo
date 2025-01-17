FROM ktbbq/pigchacli

ADD pigchacli /usr/bin/pigchacli

RUN mkdir -p /root/.config/pigcha && chmod +x /usr/bin/pigchacli
ADD acc.json /root/.config/pigcha/
ADD config.ini /root/.config/pigcha/


CMD ["/bin/sh","-c","/usr/bin/pigchacli --start"]
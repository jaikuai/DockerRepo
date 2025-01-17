FROM williamyeh/java8

ENV LANG=C.UTF-8 TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App


CMD ["/bin/sh","-c","/usr/bin/java -jar /home/App.jar --spring.application.name=${PRO_NAME} --spring.profiles.active=${PRO_ENV}"]
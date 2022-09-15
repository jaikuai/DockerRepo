FROM bridg/java8

ENV TZ="Asia/Shanghai" PRO_ENV=dev PRO_NAME=App


CMD ["/bin/sh","-c","/usr/bin/java -jar /home/App.jar --spring.application.name=${PRO_NAME} --spring.profiles.active=${PRO_ENV}"]
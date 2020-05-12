FROM rpi.it5000.com:5000/java:8-jre-alpine

ADD glowroot /home/glowroot
WORKDIR /home

CMD ["/bin/sh","-c","/usr/bin/java -jar -javaagent:/home/glowroot/glowroot.jar /home/App.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}"]
FROM rpi.it5000.com:5000/java:8-jre-alpine

ADD pinpoint-agent-2.4.2 /home/pinpoint-agent-2.4.2
WORKDIR /home

CMD ["/bin/sh","-c","/usr/bin/java -jar -javaagent:/home/pinpoint-agent-2.4.2/pinpoint-bootstrap-2.4.2.jar -Dpinpoint.agentId=${PRO_NAME} -Dpinpoint.applicationName=${PRO_NAME} /home/App.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}"]
#!/bin/sh

if [ "$PRO_ENV" != "prd" ]; then
  /usr/bin/java -server -javaagent:/home/glowroot/glowroot.jar -jar /home/${PRO_NAME}.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}
else
  /usr/bin/java -server -jar /home/${PRO_NAME}.jar --spring.profiles.active=${PRO_ENV} --spring.application.name=${PRO_NAME}
fi


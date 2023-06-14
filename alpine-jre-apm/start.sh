#!/bin/sh

if [ "$PRO_ENV" != "prd" ]; then
  /usr/bin/java -server -javaagent:/home/pinpoint-agent-2.4.2/pinpoint-bootstrap-2.4.2.jar -Dpinpoint.agentId=${PRO_NAME} -Dpinpoint.applicationName=${PRO_NAME} -jar /home/${PRO_NAME}.jar --spring.profiles.active=${PRO_ENV}
else
  /usr/bin/java -server -jar /home/${PRO_NAME}.jar --spring.profiles.active=${PRO_ENV}
fi


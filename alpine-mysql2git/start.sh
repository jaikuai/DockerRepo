#!/bin/sh


git clone --depth=1 $GIT_URL data \
	&& cd data && rm -f $FILE_PATH \
	&& mysqldump -hmysql -uroot -p$MYSQL_PASSWORD --opt --all-databases |gzip > $FILE_PATH \
	&& git add $FILE_PATH \
	&& git commit -m $(date '+%Y-%m-%d %H:%M:%S') \
	&& git push origin master \
	&& rm -rf ../data

sleep 1h
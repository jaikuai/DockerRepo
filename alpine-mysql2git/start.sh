#!/bin/sh


git clone --depth=1 https://$GIT_USER:$GIT_PASS@git.oschina.net$GIT_URL data \
	&& cd data && rm -rf $MY_DIR && mkdir -p $MY_DIR \
	&& mysqldump -hmysql -ubackup -p$MYSQL_PASSWORD --opt --all-databases |gzip > $MY_DIR/all.db.sql.gz \
	&& git add $MY_DIR/all.db.sql.gz \
	&& git commit -m $(date '+%Y-%m-%d%H:%M:%S') \
	&& git push origin master \
	&& rm -rf ../data

sleep 1h
FROM hypriot/rpi-alpine-scratch

ENV TZ="Asia/Shanghai" USER="svn" PASS="123456"

# Install subversion
RUN apk add --update && apk add tzdata subversion && rm -rf /var/cache/apk/* \ 
	&& mkdir -p /data \
	&& svnadmin create /data \
	&& echo "[users]" > /data/conf/passwd \
	&& echo "$USER = $PASS" >> /data/conf/passwd \
	&& echo "[/]" > /data/conf/authz \
	&& echo "$USER = rw" >> /data/conf/authz



CMD ["/bin/sh","-c","/usr/bin/svnserve -d -r /data --log-file=/var/log/svn.log && /usr/bin/tail -f /var/log/svn.log"]

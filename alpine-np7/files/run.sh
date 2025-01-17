#!/bin/sh
mkdir -p /run/nginx



/usr/sbin/php-fpm7

/usr/sbin/nginx

echo never > /sys/kernel/mm/transparent_hugepage/enabled
/usr/bin/redis-server
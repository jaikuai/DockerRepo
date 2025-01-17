#!/bin/sh

# start php-fpm
exec /usr/bin/php-fpm -R &

# start nginx
nginx
#!/bin/sh

# start php-fpm
exec /usr/bin/php-fpm5 -R &

# start nginx
nginx

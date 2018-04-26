#!/bin/sh

redis-server &
python3 /crysadm/crysadm_helper.py >> /tmp/error 2>&1 &
python3 /crysadm/crysadm.py
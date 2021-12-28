FROM ubuntu:21.04

ADD  ./instantclient_21_4 /home/instantclient_21_4/lib

ENV TZ="Asia/Shanghai" ORACLE_HOME="/home/instantclient_21_4"

WORKDIR /home/project

RUN echo "deb http://mirrors.aliyun.com/ubuntu/ hirsute main restricted universe multiverse" > /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ hirsute main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ hirsute-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ hirsute-security main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ hirsute-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ hirsute-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ hirsute-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ hirsute-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ hirsute-proposed main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ hirsute-proposed main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1 python3 python3-pip proj-bin

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple pyproj==3.1.0 xlrd xlutils pymysql requests cx_oracle

RUN cp -rf /home/instantclient_21_4/lib/lib* /usr/lib/

ENTRYPOINT /usr/bin/python3
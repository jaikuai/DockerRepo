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

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1 python3 python3-pip proj-bin wget

RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyproj==3.1.0 xlrd xlutils pymysql requests cx_oracle apscheduler pandas pyecharts web.py elasticsearch

RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz && tar -xvf ta-lib-0.4.0-src.tar.gz && cd ta-lib && ./configure --prefix=/usr && make && make install
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple ta-lib


RUN cp -rf /home/instantclient_21_4/lib/lib* /usr/lib/

# ENTRYPOINT /usr/bin/python3
CMD ["/bin/sh","-c","/usr/bin/python3 main.py"]
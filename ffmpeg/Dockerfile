FROM nas.fast-fun.cn:5000/ubuntu:21.04


ENV TZ="Asia/Shanghai" QT_DEBUG_PLUGINS=1
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

RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y libaio1 libxcb-xinerama0 python3 python3-pip wget ffmpeg

RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python pandas pyyaml==5.4.1 requests openpyxl

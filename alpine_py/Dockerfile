FROM alpine

WORKDIR /home

COPY simhei.ttf /usr/share/fonts/simhei.ttf

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories

RUN apk --update --no-cache add tzdata ttf-dejavu fontconfig python3 py3-pip python3-dev build-base libffi-dev openssl-dev cython zlib-dev musl-dev libc-dev libffi-dev gcc g++ git
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
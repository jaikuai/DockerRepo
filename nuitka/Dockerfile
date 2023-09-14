FROM python:3.9-alpine

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories
RUN apk --update --no-cache add cython gcc g++ libffi-dev zlib-dev musl-dev binutils linux-headers patchelf ccache
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U nuitka
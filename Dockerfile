FROM ubuntu
COPY . /seq2seq
WORKDIR /seq2seq
# install and create py37 env1
# RUN apt-get update \
#     && apt-get upgrade \
#     && apt-get install ca-certificates \
#     && rm /etc/apt/sources.list \
#     && mv ./sources.list /etc/apt/sources.list \
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update \
    && apt-get install -y wget gcc automake autoconf libtool make zlib* libffi-dev\
    && wget https://npm.taobao.org/mirrors/python/3.7.8/Python-3.7.8.tgz \
    && tar -zxvf Python-3.7.8.tgz \
    && cd Python-3.7.8 \
    && ./configure --prefix=/usr/local/python3.7.8 \
    && make \
    && make install \
    # && PATH=$PATH:$HOME/bin:/usr/local/python3.7.8/bin \
    && cd ../ \
    && rm -rf ./python3.7.8* \
    && pip3 install -r ./requirements.txt -i \
    http://pypi.douban.com/simple/ --trusted-host pypi.douban.com \
    && ln -s /usr/local/python3.7.8/bin/python3.7 /usr/bin/python \
    && PATH=/usr/bin:$PATH
# environment variables
ENV PYTHONPATH "/usr/local/python3.7.8/bin/:$PYTHONPATH"
# run the experiment
# CMD python run_exp.py
CMD python run_exp.py
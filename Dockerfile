FROM ubuntu:22.04

LABEL MAINTAINER="ABCbit_AWS1 TEAM_ Dongwoo Lee, Shinhyung Kim, Minsu Park, Jihee Seo, Donghee Shin DevOps Project"

LABEL version="abcbit:1.0"

WORKDIR /

SHELL ["/bin/bash", "-c"]

RUN mkdir /BTC_edu_final
COPY . /BTC_edu_final

RUN mkdir -p /var/log/gunicorn \
&& apt-get update -y \
&& apt-get install libmysqlclient-dev gcc python3-dev python3-pip python3-venv nginx  -y \
&& echo '127.0.0.1 abcbit.shop' >> /etc/hosts \
&& python3 -m venv /BTC_edu_final/venv \
&& source /BTC_edu_final/venv/bin/activate \
&& pip3 install -r /BTC_edu_final/requirements.txt \
&& echo 'daemon off;' >> /etc/nginx/nginx.conf 

COPY ./proxy_gunicorn.conf /etc/nginx/sites-available/

RUN rm -rf /etc/nginx/sites-available/default && rm -rf /etc/nginx/sites-enabled/default \ 
&& ln -s /etc/nginx/sites-available/proxy_gunicorn.conf /etc/nginx/sites-enabled/default \
&& rm -rf /BTC_edu_final/requirements.txt \
&& rm -rf /var/lib/apt/lists/*
WORKDIR /BTC_edu_final 

CMD ["/bin/bash","-c","venv/bin/gunicorn -b 0:8000 --access-logfile /var/log/gunicorn/access.log --error-logfile /var/log/gunicorn/error.log --daemon --reload abcbit.wsgi:application;nginx"]


FROM debian:latest
MAINTAINER ggerardy
ENV TZ=Europe/Russia

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
	tzdata \
	postgresql \
	postgresql-contrib \
	libpq-dev \
	redis-server \
	libicu-dev \
	cmake \
	g++ \
	libkrb5-dev \
	libre2-dev \
	ed \
	pkg-config \
	graphicsmagick \
	runit \
	golang \
	make \
	wget \
	lbzip2 \
	nodejs \
	curl \
	git \
	nodejs \
	build-essential \
	yarn

RUN curl -sSL https://get.rvm.io | bash

WORKDIR /root
RUN wget http://download.redis.io/releases/redis-5.0.4.tar.gz
RUN tar xzf redis-5.0.4.tar.gz
RUN cd redis-5.0.4 && make && make install

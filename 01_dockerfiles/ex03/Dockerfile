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

WORKDIR /root
RUN wget http://download.redis.io/releases/redis-5.0.4.tar.gz
RUN tar xzf redis-5.0.4.tar.gz
RUN cd redis-5.0.4 && make && make install

WORKDIR /
RUN curl -sSL https://get.rvm.io | bash
ENV PATH $PATH:/usr/local/rvm/bin
RUN rvm install 2.5.3
ENV PATH $PATH:/usr/local/rvm/rubies/ruby-2.5.3/bin

RUN apt-get update && apt-get install -y \
	vim \
	unzip

WORKDIR /root
RUN rm -f redis-5.0.4.tar.gz

RUN apt-get remove -y cmdtest
RUN mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
ENV PATH $PATH:/root/homebrew/bin
RUN brew install yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install -y nodejs
#RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN gem install gitlab-development-kit
RUN gdk init gdk
#RUN cd ./gdk && gdk install

FROM debian:latest
MAINTAINER ggerardy

ENV TZ=Europe/Russia
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y sudo

RUN useradd -ms /bin/bash docker && echo "docker:docker" | chpasswd && adduser docker sudo
RUN echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
WORKDIR /home/docker
USER docker

#TODO delete nodejs
RUN sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install -y \
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
	make \
	wget \
	lbzip2 \
	nodejs \
	curl \
	git \
	build-essential \
	sudo \
	vim \
	unzip

RUN wget http://download.redis.io/releases/redis-5.0.4.tar.gz
RUN tar xzf redis-5.0.4.tar.gz
RUN cd redis-5.0.4 && make && sudo make install
RUN rm -f redis-5.0.4.tar.gz

RUN curl -sSL https://get.rvm.io | bash
ENV PATH $PATH:/usr/local/rvm/bin:/home/docker/.rvm/bin
RUN rvm install 2.5.3
ENV PATH $PATH:/home/docker/.rvm/rubies/ruby-2.5.3/bin/
RUN /home/docker/.rvm/src/rubygems-3.0.3/bin/gem uninstall --all -Iax
RUN gem uninstall --all -Iax
RUN gem install -f bundler -v 1.17.3
####RUN rm -rf $(find / -name 'bundler')

RUN mkdir homebrew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C homebrew
ENV PATH $PATH:/home/docker/homebrew/bin
RUN brew install yarn
RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo bash
RUN sudo apt-get install -y nodejs
###RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN wget https://storage.googleapis.com/golang/go1.12.1.linux-amd64.tar.gz
RUN tar -xvf go1.12.1.linux-amd64.tar.gz
RUN rm -f go1.12.1.linux-amd64.tar.gz
RUN sudo mv go/ /usr/local
ENV GOROOT /usr/local/go
RUN mkdir -p gopath
ENV GOPATH /home/docker/gopath
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH

####ENV PATH $PATH:/usr/local/rvm/rubies/ruby-2.5.3/bin/gdk:/home/docker/homebrew/bin:/usr/local/rvm/bin
RUN gem install gitlab-development-kit
RUN gdk init gdk

#RUN cd ./gdk && gdk install






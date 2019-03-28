FROM ubuntu:latest
MAINTAINER ggerardy

RUN apt-get update && apt-get install -y \
	vim \
	wget \
	lbzip2 \
	make \
	gcc \
	gnupg \
	ruby \
	nodejs

	#mysql-server \
	#mysql-client

WORKDIR /root
RUN wget http://download.redis.io/releases/redis-5.0.4.tar.gz
RUN tar xzf redis-5.0.4.tar.gz
RUN cd redis-5.0.4 && make && make install


RUN mkdir -p ~/.gnupg
RUN echo "disable-ipv6" >> ~/.gnupg/dirmngr.conf

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list
RUN apt-get update && apt-get install -y software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

WORKDIR /
USER postgres
RUN /etc/init.d/postgresql start &&\
	psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\
	createdb -O docker docker

RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

#RUN /usr/lib/postgresql/9.3/bin/postgres -D /var/lib/postgresql/9.3/main -c config_file=/etc/postgresql/9.3/main/postgresql.conf &

USER root
WORKDIR /root
#	PostgreSQL \
#	ruby \
#	nodejs \
#	redis \
#	sidekiq \
#	Prometheus \
#	git \

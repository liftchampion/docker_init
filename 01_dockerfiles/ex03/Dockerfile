FROM ubuntu:latest
MAINTAINER ggerardy

ENV TZ=Europe/Russia
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y \
		vim \
		ca-certificates \
		curl \
		openssh-server \
		wget \
		tzdata

RUN curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | bash
RUN apt-get install gitlab-ce

EXPOSE 80 443 22

RUN mkdir -p /etc/ssl/private && \
		mkdir -p /etc/ssl/certs && \
		mkdir -p /etc/gitlab/ssl 
RUN openssl genrsa -passout pass:x -out server.pass.key 2048
RUN openssl rsa -passin pass:x -in server.pass.key -out server.key
RUN rm server.pass.key
RUN openssl req -new -key server.key -out server.csr \
			-subj "/C=UK/ST=GGgg/L=GGgg/O=GGgg/OU=GGgg/CN=ggggggg.com"
RUN openssl x509 -req -days 365 -in server.csr -signkey server.key \
			-out server.crt && \
		chmod 777 /etc/gitlab/ssl && \
		cp server.key server.crt /etc/gitlab/ssl
RUN echo "nginx['ssl_certificate'] = \"/etc/gitlab/ssl/server.crt\""  >> /etc/gitlab/gitlab.rb && \
	echo "nginx['ssl_certificate_key'] = \"/etc/gitlab/ssl/server.key\"" >> /etc/gitlab/gitlab.rb \
	echo "nginx['redirect_http_to_https'] = 80" >> /etc/gitlab/gitlab.rb

ENTRYPOINT cat /etc/gitlab/gitlab.rb | awk -v ip=$IP '{if ($1 == "external_url") {$2 = \'ip":4242"\'} print $0}' > /etc/gitlab/gitlab.rb && bash

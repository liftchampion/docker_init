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

RUN cat /etc/gitlab/gitlab.rb | awk -v ip=$IP '{if ($1 == "external_url") {$2 = ip":4242"} print $0}' > /etc/gitlab/gitlab.rb
EXPOSE 80 443 22

ENTRYPOINT cat /etc/gitlab/gitlab.rb | awk -v ip=$IP '{if ($1 == "external_url") {$2 = ip":4242"} print $0}' > /etc/gitlab/gitlab.rb && bash

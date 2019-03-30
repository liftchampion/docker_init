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

EXPOSE 80 443 22 22222

RUN mkdir -p /etc/ssl/private && \
		mkdir -p /etc/ssl/certs && \
		mkdir -p /etc/gitlab/ssl
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
	-subj "/C=UK/ST=GGgg/L=GGgg/O=GGgg/OU=GGgg/CN=192.168.99.100" \
	-keyout /etc/gitlab/ssl/key.key \
	-out /etc/gitlab/ssl/cert.crt

RUN echo "nginx['ssl_certificate'] = \"/etc/gitlab/ssl/cert.crt\""  >> /etc/gitlab/gitlab.rb && \
	echo "nginx['ssl_certificate_key'] = \"/etc/gitlab/ssl/key.key\"" >> /etc/gitlab/gitlab.rb && \
	echo "nginx['redirect_http_to_https'] = true" >> /etc/gitlab/gitlab.rb && \
	echo "nginx['redirect_http_to_https_port'] = 80" >> /etc/gitlab/gitlab.rb && \
	echo "letsencrypt['enable'] = false" >> /etc/gitlab/gitlab.rb && \
	echo "gitlab_rails['gitlab_ssh_host'] = '192.168.99.100'" >> /etc/gitlab/gitlab.rb && \
	echo "gitlab_rails['gitlab_shell_ssh_port'] = 22222" >> /etc/gitlab/gitlab.rb


RUN (/opt/gitlab/embedded/bin/runsvdir-start &) && gitlab-ctl reconfigure
RUN usermod -a -G $(cat /etc/group | awk -F ':' '{print $1}' | tr '\n' ',' | sed 's/,$//g') git
RUN usermod -a -G $(cat /etc/group | awk -F ':' '{print $1}' | tr '\n' ',' | sed 's/,$//g') gitlab-www

RUN echo "Port 22222" >> /etc/ssh/ssh_config
RUN echo "Port 22222" >> /etc/ssh/sshd_config
RUN mkdir -p /run/sshd

ENTRYPOINT cat /etc/gitlab/gitlab.rb | awk -v ip=$IP -v q="'" '{if ($1 == "external_url") {$2 = q"https://"ip"/"q} print $0}' > tmp.gg && \
			cat tmp.gg > /etc/gitlab/gitlab.rb && \
			/usr/sbin/sshd && \
			rm -f tmp.gg && \
			(/opt/gitlab/embedded/bin/runsvdir-start &) && \
			gitlab-ctl reconfigure && \
			tail -f /dev/null

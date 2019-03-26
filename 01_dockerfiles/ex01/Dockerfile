FROM debian:latest
MAINTAINER ggerardy
RUN apt-get update && apt-get install -y \
	vim \
	wget \
	lbzip2 \
	systemd
WORKDIR /root
RUN wget https://files.teamspeak-services.com/releases/server/3.7.0/teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN tar xvf teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN mv teamspeak3-server_linux_amd64/* ./
RUN rm -f teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN touch .ts3server_license_accepted
EXPOSE 9987/udp
ENTRYPOINT (exec /root/ts3server_startscript.sh start inifile=/root/ts3server.ini) && (exec /bin/bash)
#ENTRYPOINT exec echo 1337 && /bin/bash
#ENTRYPOINT ["/root/ts3server_startscript.sh", "start", "inifile=/root/ts3server.ini"]
#CMD ["/bin/bash"]
#CMD ["", "/bin/bash"]

FROM debian:latest
MAINTAINER ggerardy
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y vim
RUN apt-get install -y wget
RUN apt-get install -y lbzip2
RUN apt-get install -y systemd
RUN cd && wget https://files.teamspeak-services.com/releases/server/3.7.0/teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN cd && tar xvf teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN cd && mv teamspeak3-server_linux_amd64/* ./
RUN cd && rm -f teamspeak3-server_linux_amd64-3.7.0.tar.bz2
RUN cd && touch .ts3server_license_accepted
VOLUME ~/SCHOOL/docker-init/01_dockerfiles/ex01
EXPOSE 9987/udp
ENTRYPOINT (exec /root/ts3server_startscript.sh start inifile=/root/ts3server.ini) && (exec /bin/bash)
#ENTRYPOINT exec echo 1337 && /bin/bash
#ENTRYPOINT ["/root/ts3server_startscript.sh", "start", "inifile=/root/ts3server.ini"]
#CMD ["/bin/bash"]
#CMD ["", "/bin/bash"]

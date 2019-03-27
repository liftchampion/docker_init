FROM ruby:latest
MAINTAINER ggerardy
RUN apt-get update && apt-get install -y \
	vim \
	nodejs
RUN gem install \
	rails \
	bundler
RUN gem update bundler

WORKDIR /opt/app/
ONBUILD COPY ./app2 /opt/app/
ONBUILD RUN bundle install
ONBUILD RUN bundle exec rake db:migrate
ONBUILD RUN bundle exec rake db:seed

EXPOSE 3000

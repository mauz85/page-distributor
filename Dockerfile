FROM debian:jessie
USER root
RUN apt-get -y update 
RUN apt-get install -y apache2
RUN a2enmod proxy
RUN a2enmod proxy_http
RUN service apache2 restart

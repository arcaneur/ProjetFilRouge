FROM mariadb:latest

ENV MYSQL_ROOT_PASSWORD=apache
ENV MYSQL_DATABASE=SalleFetes
ENV MYSQL_USER=Frantz
ENV MYSQL_PASSWORD=apache2

COPY ./init.sql /docker-entrypoint-initdb.d/

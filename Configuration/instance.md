**Database Preparation step**

download mysql repo

_wget http://repo.mysql.com/mysql-apt-config_0.8.17-1_all.deb_

install it

_sudo apt install ./mysql-apt-config_0.8.17-1_all.deb_

Install mysql server

_sudo apt update
sudo apt install mysql-server_

Securing mysql installation

_sudo mysql_secure_installation_

create user and granting privileges

_CREATE USER 'basoca'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON * . * TO 'basoca'@'localhost';
FLUSH PRIVILEGES;_

Create database and import the data

_sudo mysql
mysql> create database basoca;
mysql> exit;
mysql -u basoca -p basoca < dataset.sql_


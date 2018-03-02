#!/usr/bin/env bash

# install requirements packages
sudo apt-get update
sudo apt-get install -y nginx uwsgi uwsgi-plugin-python3 libmysqlclient-dev python3.5-dev python3.5-venv
sudo apt-get install -y mysql-server memcached
mysql -uroot -e "create database shop CHARACTER SET utf8 COLLATE utf8_general_ci;" -p

#cd /opt/posuda
#python3.5 -m venv env
#. env/bin/activate
#pip install --upgrade pip
#pip insatll -r requirements.txt

# hosts config
sudo cp -f /vagrant/vagrant/hosts /etc/hosts
sudo apt-get install
#CREATE DATABASE viaescort CHARACTER SET utf8 COLLATE utf8_general_ci;

# nginx config
sudo cp /vagrant/vagrant/nginx/vizhu.conf /etc/nginx/sites-available/vizhu.conf
sudo chmod 644 /etc/nginx/sites-available/vizhu.conf
sudo ln -s -f /etc/nginx/sites-available/vizhu.conf /etc/nginx/sites-enabled/vizhu.conf
sudo service nginx restart
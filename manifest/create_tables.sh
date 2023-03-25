#!/bin/bash

sudo mysql -e "USE identity;"

#create table user
sudo mysql -e "CREATE TABLE IF NOT EXISTS user(
        `login` varchar (50) not null,
        `first_name` varchar (50) not null,
        `last_name` varchar (50) not null,
        PRIMARY KEY (`login`));"

#table user_pw
sudo mysql -e  "CREATE TABLE IF NOT EXISTS user_pw(
        `login_pw` varchar (50),
        `password` text not null,
        CONSTRAINT FK_login_pw FOREIGN KEY (`login_pw`) REFERENCES user(`login`))";

sudo mysql -e "USE config_generator";

#table server_web
sudo mysql -e  "CREATE TABLE IF NOT EXISTS server_web(
        `server_name_web`varchar (50) not null,
        `ip_address_serv_web` varchar (50) not null,
        `root` varchar (50) not null,
        `location` varchar (50) not null,
        `error_page` varchar (50) not null,
        PRIMARY KEY (`server_name`))";

#table load_balancer
sudo mysql -e  "CREATE TABLE IF NOT EXISTS load_balancer(
        `server_name_load_balancer`varchar (50) not null,
        `ip_address_load_balancer` varchar (50) not null;
        `location_serv_web` varchar (50) not null,
        PRIMARY KEY (`server_name`),
        CONSTRAINT FK_location FOREIGN KEY (`location_serv_web`) REFERENCES server_web(`server_name_web`)))";

#table reverse_proxy
sudo mysql -e "CREATE TABLE IF NOT EXISTS reverse_proxy(
        `server_name_reverse_proxy`varchar (50) not null,
        `ip_address_reverse_proxy` varchar (50) not null;
        `proxy_bind` varchar (50) not null,
        `proxy_pass` varchar (50) not null,
        PRIMARY KEY (`server_name`),
        CONSTRAINT FK_location FOREIGN KEY (`location_serv_web`) REFERENCES server_web(`server_name_web`)))";
#!/bin/bash

sudo mysql -u root -p'passwordDbUniv01' -e "UPDATE mysql.user SET Password = PASSWORD('passwordDbUniv01') WHERE User = 'root';"

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
        CONSTRAINT FK_login_pw FOREIGN KEY (`login_pw`) REFERENCES user(`login`));"
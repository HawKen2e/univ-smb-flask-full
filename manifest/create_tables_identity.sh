#!/bin/bash
use identity;

CREATE TABLE IF NOT EXISTS user (
        login varchar (50) not null,
        first_name varchar (50) not null,
        last_name varchar (50) not null,
        PRIMARY KEY (login));

#table user_pw
CREATE TABLE IF NOT EXISTS user_pw (
        login_pw varchar (50),
        password text not null,
        CONSTRAINT FK_login_pw FOREIGN KEY (login_pw) REFERENCES user(login));
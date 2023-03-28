#!/bin/bash
USE config_generator;

#table server_web
CREATE TABLE IF NOT EXISTS `server_web` (
        server_name_web varchar (50) not null,
        ip_address_serv_web varchar (50) not null,
        root varchar (50) not null,
        location varchar (50) not null,
        error_page varchar (50) not null,
        PRIMARY KEY (server_name));

#table load_balancer
CREATE TABLE IF NOT EXISTS `load_balancer` (
        server_name_load_balancer varchar (50) not null,
        ip_address_load_balance varchar (50) not null;
        location_serv_web varchar (50) not null,
        PRIMARY KEY (server_name),
        CONSTRAINT FK_location FOREIGN KEY (location_serv_web) REFERENCES server_web(server_name_web));

#table reverse_proxy
CREATE TABLE IF NOT EXISTS `reverse_proxy` (
        server_name_reverse_proxy varchar (50) not null,
        ip_address_reverse_proxy varchar (50) not null;
        proxy_bind varchar (50) not null,
        proxy_pass varchar (50) not null,
        PRIMARY KEY (server_name),
        CONSTRAINT FK_location FOREIGN KEY (location_serv_web) REFERENCES server_web(server_name_web));"
# Movie Booking App

It's a simple application with microservices architecture. More detail in [this tutorial](https://quanrong88.github.io/2018/01/15/Building-microservices-using-Flask-RestPlus-Swagger-UI-RabbitMQ-and-Nameko/) 

### Installing

* Install [Docker](https://docs.docker.com)
* Change directory to the project root forder.
*  Run this command in command line to run project
```
$ docker-compose up
```
* Create project database using following commands:
```
$ docker exec -it base-mysql bash
# mysql -u root -p quan
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.20 MySQL Community Server (GPL)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> CREATE DATABASE demodb;
Query OK, 1 row affected (0.00 sec)
```
* Create user table using following commands:
```
$ docker exec -it user-module bash
# python
Python 3.6.4 (default, Dec 21 2017, 01:35:12)
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from database import engine, metadata
>>> metadata.create_all(engine)
```
* Create movie table using following commands:
```
$ docker exec -it movie-module bash
# python
Python 3.6.4 (default, Dec 21 2017, 01:35:12)
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from database import engine, metadata
>>> metadata.create_all(engine)
```
* Create bookings table using following commands:
```
$ docker exec -it booking-module bash
# python
Python 3.6.4 (default, Dec 21 2017, 01:35:12)
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> from database import engine, metadata
>>> metadata.create_all(engine)
```
* Open web brower, type http://localhost:30/api/

### Build With

* [Flask-RESTful](https://github.com/flask-restful/flask-restful) provides the building blocks for creating a great REST API.
* [RabbitMQ](https://www.rabbitmq.com) is the most widely deployed open source message broker.
* [Nameko](https://github.com/nameko/nameko) is Python framework for building microservices
* [SQLAlchemy](https://www.sqlalchemy.org) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* [marshmallow](https://github.com/marshmallow-code/marshmallow) is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.
* [pymysql](https://github.com/PyMySQL/PyMySQL) is pure Python MySQL Client.

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, Float
import pymysql
import os
pymysql.install_as_MySQLdb()
metadata = MetaData()
movies = Table('movies', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(50)),
    Column('director', String(50)),
    Column('ranking', Float),
)
serverName = os.getenv('MYSQL_SERVER','TEST')
dbName = os.getenv('MYSQL_DATABASE','TEST')
dbUserName = os.getenv('MYSQL_USERNAME','TEST')
dbPassword = os.getenv('MYSQL_PASSWORD','TEST')
dbURI = 'mysql://%s:%s@%s/%s' % (dbUserName, dbPassword, serverName, dbName)
engine = create_engine(dbURI)

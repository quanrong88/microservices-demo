from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, ARRAY,DateTime,func
import pymysql
import os
pymysql.install_as_MySQLdb()
metadata = MetaData()
bookings = Table('bookings', metadata,
    Column('id', Integer, primary_key=True),
    Column('userId', Integer),
    Column('movieIds', String(100)),
    Column('pubDate', DateTime, onupdate=func.utc_timestamp())

)
serverName = os.getenv('MYSQL_SERVER','TEST')
dbName = os.getenv('MYSQL_DATABASE','TEST')
dbUserName = os.getenv('MYSQL_USERNAME','TEST')
dbPassword = os.getenv('MYSQL_PASSWORD','TEST')
dbURI = 'mysql://%s:%s@%s/%s' % (dbUserName, dbPassword, serverName, dbName)
engine = create_engine(dbURI)

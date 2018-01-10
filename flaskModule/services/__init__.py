import os
serverName = os.getenv('BROKER_NAME','TEST')
userName = os.getenv('BROKER_USERNAME','TEST')
password = os.getenv('BROKER_PASSWORD','TEST')
brokerURI = "amqp://%s:%s@%s" % (userName, password, serverName)
CONFIG = {'AMQP_URI': brokerURI}

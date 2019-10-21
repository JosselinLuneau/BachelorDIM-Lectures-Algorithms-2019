import os
import pika
import time
from model.Reader import Reader

def read(amqp_url, queueName, concurrency=False, sleep=False, auto_ack=True):
    '''Function that read datas from amqp queue

        @param amqp_url : a string
        @param queueName : a string
        @param auto_ack : a boolean
    '''
   
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    reader = Reader(1, queueName, url)
    reader.InitChannel()
    reader.Consume()

''' TESTS '''
'''# Get session config
import config
import getpass 
  
user = getpass.getuser() 
amqp_url=config.COUD_AMQP_URL # get url of broker

read(amqp_url, 'presentation', user)'''
import config
from model.Reader import Reader

def read(amqp_url, queueName, concurrency=False, sleep=False, auto_ack=True):
    '''Function that read datas from amqp queue

        @param amqp_url : a string
        @param queueName : a string
        @param concurrency :  a boolean
        @sleep : a boolean
        @param auto_ack : a boolean
    '''

    reader = Reader(1, config.CLOUD_AMQP_URL, queueName)
    reader.Consume()

''' TESTS '''
'''# Get session config
import config
import getpass 
  
user = getpass.getuser() 
amqp_url=config.COUD_AMQP_URL # get url of broker

read(amqp_url, 'presentation', user)'''
import os
import pika
import config

queueName = 'post'

def InitConnection(timeout = 5):
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',config.CLOUD_AMQP_URL)
    params = pika.URLParameters(url)
    params.socket_timeout = timeout

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    return connection
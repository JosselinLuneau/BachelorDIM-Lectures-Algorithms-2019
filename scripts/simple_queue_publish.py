import os
import pika

def publish(amqp_url, queueName, body, buffer=1, concurrency=False, timeout=5):
    '''Function that publish datas from amqp queue

        @param amqp_url : a string
        @param queueName : a string
        @param body : a string -> body message 
        @param buffer : an integer -> number of message
        @param timeout : an integer
    '''
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = timeout # define timeout
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    properties = pika.BasicProperties() # Init properties

     # set delivery mode for persistant message
    if concurrency:
        properties.delivery_mode=2

    # Define channel
    channel = connection.channel()
    channel.queue_declare(queue=queueName)

    #Send message
    buffer = int(buffer) + 1 # get number of message to send
    for i in range(1, buffer):
        channel.basic_publish(exchange='',
                                routing_key=queueName,
                                body=body,
                                properties=properties)
                                
        print(' [{1}] Sent \'{0}\''.format(body, i))
        
    connection.close()

''' TESTS '''
# Get session config
import config
import getpass 
  
user = getpass.getuser() 
amqp_url=config.COUD_AMQP_URL # get url of broker

publish(amqp_url, 'presentation', user)
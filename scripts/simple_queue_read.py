import os
import pika
from model.Reader import Reader

def read(amqp_url, queueName, concurrency=False, auto_ack=True):
    '''Function that read datas from amqp queue

        @param amqp_url : a string
        @param queueName : a string
        @param auto_ack : a boolean
    '''
    
    # callback to receive message
    def callback(ch, method, properties, body):
        '''Callback call when a data is fetch from cloud

            @param ch : a string
            @param method : a string
            @param properties : a boolean
            @param body : a string -> body message
        '''
        number=method.delivery_tag
        print(" [{0}] Received {1}".format(number ,body))
        ch.basic_ack(number)

    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5

    connection = pika.BlockingConnection(params) # Connect to CloudAMQP

    channel = connection.channel()
    channel.queue_declare(queue=queueName)

    # Collect datas from broker
    channel.basic_consume(queue=queueName,
                            on_message_callback=callback,                          
                            auto_ack=False)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

def TwoReader(amqp_url, queueName, concurrency=False ,auto_ack=True):
    reader1 = Reader(id=1,
                    queueName=queueName,
                    url=amqp_url)

    reader1.InitChannel()
    reader1.Consume()

    reader2 = Reader(id=2,
                    queueName=queueName,
                    url=amqp_url)

    reader2.InitChannel()
    reader2.Consume()


''' TESTS '''
'''# Get session config
import config
import getpass 
  
user = getpass.getuser() 
amqp_url=config.COUD_AMQP_URL # get url of broker

read(amqp_url, 'presentation', user)'''
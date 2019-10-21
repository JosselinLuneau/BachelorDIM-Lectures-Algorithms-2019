import os
import pika
import time

class Reader: 
    
    def __init__(self, id,queueName, url, timeout=5):
        self.id = 1
        self.queueName = queueName
        self.url = url
        self.timeout = timeout
        self.channel=''
        self.sleep = False
    
    def InitChannel(self):
        # Parse CLODUAMQP_URL (fallback to localhost)
        url = os.environ.get('CLOUDAMQP_URL',self.url)
        params = pika.URLParameters(url)
        params.socket_timeout = self.timeout

        connection = pika.BlockingConnection(params) # Connect to CloudAMQP
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queueName)
    
    def Consume(self):

        # callback to receive message
        def callback(ch, method, properties, body):
            '''Callback call when a data is fetch from cloud

                @param ch : a string
                @param method : a string
                @param properties : a boolean
                @param body : a string -> body message
            '''
            number=method.delivery_tag
            print("Reader {0} : [Message-{1}] Received {2}".format(self.id, number ,body))
            ch.basic_ack(number)
            
        def callbackSleep(ch,method, properties, body):
            '''Callback call when a data is fetch from cloud

                @param ch : a string
                @param method : a string
                @param properties : a boolean
                @param body : a string -> body message
            '''
            time.sleep(1)
            number=method.delivery_tag
            print(" [{0}] Received {1}".format(number ,body))
            ch.basic_ack(number)

        if self.sleep:
            print("Sleep Mode")
            # Collect datas from broker
            self.channel.basic_consume(queue=self.queueName,
                                on_message_callback=callbackSleep,                          
                                auto_ack=False)
        else:
            # Collect datas from broker
            self.channel.basic_consume(queue=self.queueName,
                                    on_message_callback=callback,                          
                                    auto_ack=False)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    
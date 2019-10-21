import s4_tools as tools
import time

class Reader: 
    
    def __init__(self, id, url, queueName = '', timeout=5):
        self.id = 1
        self.queueName = queueName
        self.url = url
        self.timeout = timeout
        self.channel=''
        self.sleep = False
        self.auto_ack = False

        if self.queueName == '':
            self.InitFanoutChannel()
            self.auto_ack = True
        else:
            self.InitChannel()
    
    def InitChannel(self):
        '''Function that init channel to read

            @param self : a instance
        '''
        connection = tools.InitConnection()
        
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queueName)
        
    def InitFanoutChannel(self):
            '''Function that init channel with fanout exchange

                @param self : a instance
            '''
            connection = tools.InitConnection()
        
            self.channel = connection.channel()
            self.channel.exchange_declare(exchange='posts',
                             exchange_type='fanout')
    
            result= self.channel.queue_declare(exclusive=True,
                                        queue = '')
            
            self.queueName = result.method.queue # et the queuname
            
            self.channel.queue_bind(exchange='posts',
                            queue = self.queueName)
    
    def Consume(self):
        '''Function that sart the channel consume

            @param self : a instance
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
            print("Reader {0} : [Message-{1}] Received {2}".format(self.id, number ,body))
            if self.auto_ack == False:
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
            # Collect datas from broker
            self.channel.basic_consume(queue=self.queueName,
                                on_message_callback=callbackSleep,                          
                                auto_ack=self.auto_ack)
        else:
            # Collect datas from broker
            self.channel.basic_consume(queue=self.queueName,
                                    on_message_callback=callback,                          
                                    auto_ack=self.auto_ack)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    
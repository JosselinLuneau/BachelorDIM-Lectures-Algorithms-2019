# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Test d'un flux d'information PC->CloudAMQP->PC
Test step 1: avec le mode 'SEND' ligne 14, lancer plusieurs fois le script pour lancer plusieurs messages dans la file dédiée dans cloudamqp
Test step 2: modifier la ligne 14 en mettant autre chose que 'SEND' dans la variable mode et lancer le script. Celui ci doit alors dépiler les messages envoyés dans le cloud et les afficher
"""
#import urlparse
import os
import pika
import config


mode='SEND' #set 'SEND' mode is you will to send rather than receive messages


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


amqp_url=config.COUD_AMQP_URL # get url of broker

# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='hello')

#Send message
if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
                          
    print(" [x] Sent 'Hello World!'")
    
    connection.close()
else: # Collect datas from broker
        
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,                          
                          auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


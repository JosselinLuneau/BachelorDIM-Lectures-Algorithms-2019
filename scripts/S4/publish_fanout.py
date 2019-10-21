import config
import pika
import s4_tools as tools

def publish_fanout():
    connection = tools.InitConnection()
    
    channel = connection.channel()
    channel.exchange_declare(exchange='posts',
                             exchange_type='fanout')
    
    channel.basic_publish(exchange='posts',
                          routing_key='',
                          body='message')
    print("send")

publish_fanout()
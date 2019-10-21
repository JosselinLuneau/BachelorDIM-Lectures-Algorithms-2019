import config
from model.Reader import Reader

def read_subscriber():
    
    reader = Reader(1, config.CLOUD_AMQP_URL)
    reader.Consume()

read_subscriber()
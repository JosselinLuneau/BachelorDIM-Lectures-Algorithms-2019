import argparse
import config
import getpass # Get session config

# Config variables
user = getpass.getuser() 
amqp_url=config.COUD_AMQP_URL # get url of broker
queueName='presentation'

# Creae arguments
parser = argparse.ArgumentParser('Publish/Consume data from queue (CloudAMQP).')
parser.add_argument('-r', '--read', help='Read mode', action='store_true') # Create argument to choose read mode
parser.add_argument('-n', '--number', type=int ,default=1, help='Define number of message to send (Default: 1)') # Create argument to count number of message publish
parser.add_argument('-c', '--concurrency',  help='Concurency mode (Default false)', action='store_true') # Create to set concurrency mode when publish

# Get args
args = parser.parse_args()
concurrency = args.concurrency
if args.read:
   import simple_queue_read as sqr
   sqr.TwoReader(amqp_url, queueName, concurrency)
else:
    import simple_queue_publish as sqp
    sqp.publish(amqp_url, queueName, user, args.number, concurrency)

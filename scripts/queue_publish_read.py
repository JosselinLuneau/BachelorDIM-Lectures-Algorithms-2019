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
parser.add_argument('-c', '--concurrency',  help='Concurency mode (Default false)', action='store_true') # Create argument to set concurrency mode when publish
parser.add_argument('-s', '--sleep', help='Add sleep time during reading', action='store_true') # Create argument to set delay on response receiving


# Get args
args = parser.parse_args()
concurrency = args.concurrency
sleep = bool(args.sleep)
if args.read:
   import simple_queue_read as sqr
   sqr.read(amqp_url, queueName, concurrency, sleep)
else:
    import simple_queue_publish as sqp
    sqp.publish(amqp_url, queueName, user, args.number, concurrency)

import pika
from pika.credentials import ExternalCredentials
from optparse import OptionParser
import ssl
import os
import json
import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


###############################################
# Callback function that handles messages and print logs
def callback(channnel, method, properties, body):
        msg = json.loads(body.decode("utf-8"))
        timestamp = msg['timestamp']
        resourceUri = msg['resourceUri']
        resource = msg['resource']
        changeType = msg['changeType']
        print ("%s: Message received:" % (timestamp))
        print ("Routing Key: %s" % (method.routing_key))
        print ("Change Type: %s" % (changeType))
        print ("Resource URI: %s" % (resourceUri))
        print ("Resource: %s" % (resource))
        log = open("%s\\OVF664\\log.txt" % (path), 'a')
        log.write(timestamp + '\n+' + method.routing_key + '\n' + changeType + '\n')
        log.writelines(resourceUri)
        log.write('\n')
        try:
            for (key, item) in resource.items():
                log.writelines(key)
                log.write(': ')
                if item is None:
                    log.write('None')
                elif item is False:
                    log.write('False')
                else:
                    log.writelines(str(item))
                log.write('\n')
        except:
            log.writelines(resource)
        log.write("\n\n")
        log.close()

# Process
# get all necessary certificates from OneView
logging.basicConfig()
# Set optparse
parser = OptionParser()
parser.add_option('--ht', '--host', dest='host', help='Pika server to connect to (default: %default)', default='localhost')
parser.add_option('--li', '--listen', dest='listen', help='#:listen all;\nresource-category.change-type.uri\n(Example1:enclosures.*./rest/enclosures/Enc1234\n Example2:server-hardware.# \nExample3:*.Created.#); \nall change types: Created, Updated, and Deleted; (default: %default)', default='#')
options, args = parser.parse_args()
# appliance_cred={'address':'15.114.113.166','userName':'administrator','password':'hpvse123','authLoginDomain':'LOCAL'}
appliance_cred = {'address': options.host}

# Setup our ssl options
path = os.getcwd()

try:
    ssl_options = ({"ca_certs": "%s\\OVF664\\caroot.pem" % (path),
                    "certfile": "%s\\OVF664\\client.pem" % (path),
                    "keyfile": "%s\\OVF664\\key.pem" % (path),
                    "cert_reqs": ssl.CERT_REQUIRED,
                    "server_side": False,
                    "ssl_version": ssl.PROTOCOL_TLSv1_2,
                    "ciphers": "ECDHE-RSA-AES256-SHA384"})

    host = appliance_cred['address']
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host, 5671, credentials=ExternalCredentials(),
            ssl=True, ssl_options=ssl_options, socket_timeout=500))
    # ====== NEW CODE ========

# Create and bind to queue
    EXCHANGE_NAME = "scmb"
    ROUTING_KEY = "scmb." + options.listen
    channel = connection.channel()
    result = channel.queue_declare()
    queue_name = result.method.queue
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key=ROUTING_KEY)
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
# Start listening for messages
    channel.start_consuming()

except:
    print "Case1:ssl set .pem error!!! pem files do not exist or invalid\nCase2:Connect RabbitMQ error!!!"
    print "Force Exit"
    exit()

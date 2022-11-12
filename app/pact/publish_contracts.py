from pact import Consumer, Provider, Broker, verifier
from datetime import date

broker = Broker(broker_base_url="http://38.242.131.123:9292")
broker.publish("GUI",
                       "2.0.7-" + str(date.today()),
                       branch='GUI-branch',
                       pact_dir='.')

# output, logs = verifier.verify_pacts('./userserviceclient-userservice.json')
from pact import Consumer, Provider, Broker, verifier

broker = Broker(broker_base_url="http://38.242.131.123:9292")
broker.publish("GUI",
                       "2.0.4",
                       branch='consumer-branch',
                       pact_dir='.')

# output, logs = verifier.verify_pacts('./userserviceclient-userservice.json')
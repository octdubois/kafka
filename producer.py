import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from random import uniform
import time
from json import dumps

mqtt_broker = 'localhost'
mqtt_client = mqtt.Client("mqttconsumerer")
mqtt_client.connect(mqtt_broker)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))



while True:
	randNumber = uniform(20.0,21.0)
	mqtt_client.publish("jerry",randNumber)
	print('MQTT: just published ' + str(randNumber)+ 'to topic temperature3')

	producer.send('jerry', value={"temperature3": randNumber})
	print('kafka: just published'+ str(randNumber)+' to topic temperature3')
	time.sleep(3)
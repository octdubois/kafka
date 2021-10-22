import paho.mqtt.client as paho
import sys

client = paho.Client()

if client.connect("localhost",1883,60) != 0:
	print("coul not connect to MqttBroker!")
	sys.exit(-1)

client.publish("test/status","Hello from paho-mqtt!",0)

client.disconnect()
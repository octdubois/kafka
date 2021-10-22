from kafka import KafkaConsumer
import json
from influxdb import InfluxDBClient

host='localhost' 
port=8086
user = 'root'
password = 'root'

def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = 'root'
    password = 'root'
    dbname = 'example'
    dbuser = 'smly'
    dbuser_password = 'my_secret_password'
    query = 'select Float_value from cpu_load_short;'
    query_where = 'select Int_value from cpu_load_short where host=$host;'
    bind_params = {'host': 'server01'}
    json_body = [
        {
            "measurement": "cpu_load_short",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]


client = InfluxDBClient(host, port, user, password,database='test3')

consumer = KafkaConsumer(
    'jerry',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
	print('Topic Name = %s, Message=%s'%(message.topic,message.value))
	mess = message[6]['temperature3']
	mess1 = message[6]['humidity3']
	print('temp:',int(mess))
	print('hum:',int(mess1))

	json_body = [
        {
            "measurement": "temp",
            
            "fields": {
                "temp_value": mess,
                "hum_value": mess1
                
            }
        }
    ]
	client.write_points(json_body)

	
import paho.mqtt.client as mqtt
from kafka import KafkaProducer
from random import uniform
import time
from json import dumps
import requests

# Enter your API key here
api_key = "3423e87b086f1a476a8e574c1354c1b7"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "montreal"

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))


while True:
    time.sleep(300)
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"] - int(273.15)

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in celcius unit) = " +
              str(current_temperature) + 
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidity) +
              "\n description = " +
              str(weather_description))
    producer.send('jerry', value={"temperature3": current_temperature,"humidity3": current_humidity})
   
    print('kafka: just published' +
          str(current_temperature)+' to topic temperature3')

    print('kafka: just published' +
          str(current_humidity)+' to topic temperature3')
    

time.sleep(3)

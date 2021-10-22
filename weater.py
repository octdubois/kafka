# importing requests and json
import requests, json,time

import argparse

from influxdb import InfluxDBClient


# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "montreal"
API_KEY = "3423e87b086f1a476a8e574c1354c1b7"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request






i=0
n=0
while i<=10:
   time.sleep(5)
   n+=1
   if response.status_code == 200:
      # getting data in the json format
      data = response.json()
      # getting the main dict block
      main = data['main']
      # getting temperature
      temperature = main['temp']
      # getting the humidity
      humidity = main['humidity']
      # getting the pressure
      pressure = main['pressure']
      # weather report
      report = data['weather']
      print(f"{CITY:-^30}")
      print(f"Temperature: {temperature}")
      print(f"Humidity: {humidity}")
      print(n)

   else:
      # showing the error message
      print("Error in the HTTP request")



   json_body = [
        {
            "measurement": "test",
            
            "fields": {
                "temp_value": temperature,
                "n_value": n
            }
        }
    ]


   client = InfluxDBClient('localhost', 8086,database='test')
   client.write_points(json_body)


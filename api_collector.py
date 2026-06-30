import http.client
import redis
import os
from dotenv import load_dotenv

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

load_dotenv()
api_key = os.getenv("x-rapidapi-key")

headers = {
    'x-rapidapi-key': f"{api_key}",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/fivedaysforcast?latitude=41.126&longitude=29.204&lang=EN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

redis_connetor = redis.Redis(host="queue", port=6379, db=0)

redis_connetor.lpush("raw_weather_queue", data) 


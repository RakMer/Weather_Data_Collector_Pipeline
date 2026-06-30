import http.client
import redis

conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "c8c55cc0bbmsh6f146e4d5044239p12f0a5jsn15b5c56f8ccc",
    'x-rapidapi-host': "open-weather13.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("GET", "/fivedaysforcast?latitude=41.126&longitude=29.204&lang=EN", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

redis_connetor = redis.Redis(host="queue", port=6379, db=0)

redis_connetor.lpush("raw_weather_queue", data) 


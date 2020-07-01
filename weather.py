""" Using requests module to get the weather """
import requests

loc_url = "http://ipinfo.io/loc"
WEATHER_URL = "http://wttr.in/"

res = requests.get(loc_url)

# decode to unicode string and strip() to remove '\n' character
# print(res.content.decode("utf-8").strip())
loc = res.content.decode("utf-8").strip()

res = requests.get(WEATHER_URL + loc)

print(res.content.decode("utf-8"))

import json, datetime
from urllib.request import urlopen


def get_values():
    url = "http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&lang=ru&type=accurate"
    response = urlopen(url) 
    content = response.read().decode("utf-8")
    parsed = json.loads(content)
    values = dict.fromkeys(["icon", "time", "description", "temp", "temp_min", "temp_max", "humidity", "pressure", "wind_speed", "wind_degree"])
    values["icon"] = parsed["weather"][0]["icon"]
    values["time"] = datetime.datetime.fromtimestamp(parsed["dt"])
    values["description"] = parsed["weather"][0]["description"]
    values["temp"] = parsed["main"]["temp"]
    values["temp_min"] = parsed["main"]["temp_min"]
    values["temp_max"] = parsed["main"]["temp_max"]
    values["humidity"] = parsed["main"]["humidity"]
    values["pressure"] = parsed["main"]["pressure"]
    values["wind_speed"] = parsed["wind"]["speed"]
    if "deg" in parsed["wind"]:
        values["wind_degree"] = parsed["wind"]["deg"]
    else:
        values["wind_degree"] = 0
    return values
    

import json, datetime, psycopg2
from urllib.request import urlopen


def get_values():
	url = "http://api.openweathermap.org/data/2.5/weather?id=524901&units=metric&lang=ru&type=accurate"
	response = urlopen(url)
	content = response.read().decode("utf-8")
	parsed = json.loads(content)
	values = dict.fromkeys(["icon", "time", "descr", "t", "t_min", "t_max", "h", "p", "ws", "wd"])
	values["icon"] = parsed["weather"][0]["icon"]
	values["time"] = datetime.datetime.fromtimestamp(parsed["dt"])
	values["descr"] = parsed["weather"][0]["description"]
	values["t"] = parsed["main"]["temp"]
	values["t_min"] = parsed["main"]["temp_min"]
	values["t_max"] = parsed["main"]["temp_max"]
	values["h"] = parsed["main"]["humidity"]
	values["p"] = parsed["main"]["pressure"]
	values["ws"] = parsed["wind"]["speed"]
	if "deg" in parsed["wind"]:
		values["wd"] = parsed["wind"]["deg"]
	else:
		values["wd"] = 0
	return values

def insert_to_db(values):
	conn = psycopg2.connect("host='***' port=*** user='***' password='***' dbname='***'")
	cursor = conn.cursor()
	cursor.execute("""INSERT INTO weather_table("Icon", "Desc", "Time", "Temp", "Temp_Min", "Temp_Max", "Humid", "Press", "Wind_Speed", "Wind_Degree", "Created") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);""", (values["icon"], values["descr"], values["time"], values["t"], values["t_min"], values["t_max"], values["h"], values["p"], values["ws"], values["wd"], datetime.datetime.now()))
	conn.commit()
	cursor.close()
	conn.close()

insert_to_db(get_values())

from urllib.request import urlopen
import datetime, psycopg2


def get_value(currencyCode):
	url = "http://cbrates.rbc.ru/tsv/"
	date = datetime.datetime.now()
	requestUrl = url + str(currencyCode) + "/" + date.strftime("%Y/%m/%d") + ".tsv"
	response = urlopen(requestUrl)
	content = response.read()
	content = str(content).replace("1\t", "")
	value = float(content[5:-3])
	insert_to_db(value, currencyCode, date)

def insert_to_db(value, currencyCode, date):
	conn = psycopg2.connect("host='***' port=*** user='***' password='***' dbname='***'")
	cursor = conn.cursor()
	cursor.execute("""INSERT INTO currency_table("Value", "Code", "Date") VALUES (%s, %s, %s);""", (value, currencyCode, date))
	conn.commit()
	cursor.close()
	conn.close()

get_value(840)
get_value(978)

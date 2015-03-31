from datetime import date
from urllib.request import urlopen


url = "http://cbrates.rbc.ru/tsv/"
currencyCode = 840
resurl = url + str(currencyCode) + "/" + date.today().strftime("%Y/%m/%d") + ".tsv"
response = urlopen(resurl)
content = response.read()
print(content)
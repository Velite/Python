from peewee import *


database = PostgresqlDatabase('***', user='***', password='***', host='***', port=***)

class BaseModel(Model):
	class Meta:
		database = database

class Currency_Table(BaseModel):
	Id = PrimaryKeyField()
	Code = IntegerField()
	Value = FloatField()
	Date = DateTimeField()

records = Currency_Table.select().where(Currency_Table.Code == 840).order_by(Currency_Table.Date)
print(records)
for rec in records:
	print("{0!s} 1$ = {1!s}р".format(rec.Date, rec.Value))

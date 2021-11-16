import datetime 
import dateutil.relativedelta
d = datetime.datetime.strptime("2021-09-01", "%Y-%m-%d") 
d2 = d - dateutil.relativedelta.relativedelta(months=1)
print(d2)
print(d2.month)

today = datetime.date.today()
print(today.month)
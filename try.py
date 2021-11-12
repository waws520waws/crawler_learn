
import json
import requests
from datetime import datetime, date, timedelta

date_today = str(date.today())
print(date_today)
print(type(date_today))
date_today = date_today.replace('-', '')
print(date_today)

yesterday = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
print(yesterday)



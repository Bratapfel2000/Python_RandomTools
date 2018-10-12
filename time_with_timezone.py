import datetime
import pytz

#tzinfo=pytz.UTC fügt zeitzonenmoeglichkeit hinzu
dt = datetime.datetime(2018, 10, 7, 11, 54, 30, tzinfo=pytz.UTC)

dt_now = datetime.datetime.now(tz=pytz.UTC)

print(dt)
print(dt_now)
 
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

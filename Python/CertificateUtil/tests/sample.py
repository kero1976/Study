from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

# Daylight saving time
dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)

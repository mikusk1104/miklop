from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone

def dateParser(dateTimeStr):
  dateTimeObj = datetime.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%f%z')
  return dateTimeObj

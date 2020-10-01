import json, dateParser, re
from datetime import datetime

def parseDNS(message, lastTime):
  lineParsedLine = json.loads(message)

  lineDate = dateParser.dateParser(lineParsedLine['time'])
  
  #print(lastTime, lineDate)
  
  if lineDate < lastTime:
    return ''

  lineHostName = lineParsedLine["syslogtag"][:-1]
  lineParsedMsg = lineParsedLine["msg"].split()
  lineDestDomain = ''

  lineLocalIP = lineParsedMsg[2][:-1]
  if re.match(r"[a-z0-9-]*\.[a-z0-9-]", lineParsedMsg[4]):
    lineDestDomain = re.findall(r"[a-z0-9-]*\.{1,61}[a-z0-9-]*\.{1,61}$", lineParsedMsg[4])
    lineDestDomain = lineDestDomain[0][:-1]
  if lineDestDomain == '':
    return ''
# 
  
  parsedLine = lineHostName + '_DNS' + ',domain=' + lineDestDomain + ',localIP=' + lineLocalIP + ' value=1 ' + str(int(lineDate.timestamp()))
  
  return(parsedLine)

def parseDNS_cache(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])

  if lineDate < lastTime:
    return ''


  lineParsedMsg = lineParsedLine["msg"].split()
    
  lineHostName = lineParsedMsg[0][:-1]
  lineCacheSize = lineParsedMsg[2][11:]
  lineCacheUsed = lineParsedMsg[3][11:]
  lineCacheItems = lineParsedMsg[4][12:]

  parsedLine = lineHostName + '_DNS' + ' CacheSize=' + lineCacheSize + ',CacheUsed=' + lineCacheUsed + ',CacheItems=' + lineCacheItems + ' ' + str(int(lineDate.timestamp()))
 
  return(parsedLine)
import json, dateParser, re
from datetime import datetime

def parseDNS(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
      
  if lineDate < lastTime:
    return ''

  lineHostName = lineParsedLine["syslogtag"][:-1]
  lineParsedMsg = lineParsedLine["msg"].split()
  lineDestDomain = ''

  lineLocalIP = lineParsedMsg[2][:-1]

  lineParsedDomain = lineParsedMsg[4][:-1].split('.')
  domainLenght = len(lineParsedDomain)
  if domainLenght < 2:
    return ''
  lineDestDomain = lineParsedDomain[domainLenght-2] + '.' + lineParsedDomain[domainLenght-1]
  
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
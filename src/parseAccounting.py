import json, dateParser, re
from datetime import datetime

def parseAccounting(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''
  
  line = lineParsedLine["msg"]
  lineHostName = line[1:line.find(": ")]
  lineParsedMsg = line.split(";")

  for x in lineParsedMsg:
    if "bytes" in x:
      lineBytes = x[x.find("=")+1:]
    if "dst-address" in x:
      lineDST = x[x.find("=")+1:]
    if "src-address" in x:
      lineSRC = x[x.find("=")+1:]

  parsedLine = lineHostName + '_accounting' + ',DestinationIP=' + lineDST + ',SourceIP=' + lineSRC + ' bytes=' + lineBytes + ' ' + str(int(lineDate.timestamp()))
  
  return(parsedLine)

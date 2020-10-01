import json, dateParser, re
from datetime import datetime

def parseAccounting(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''
  
  lineParsedMsg = lineParsedLine["msg"].strip().split(';')

  lineHostName = lineParsedMsg[0][:lineParsedMsg[0].find(": ")]
  lineDST = lineParsedMsg[2][12:]
  lineSRC = lineParsedMsg[4][12:]
  lineBytes = lineParsedMsg[1][6:]
  
  parsedLine = lineHostName + '_accounting' + ',DestinationIP=' + lineDST + ',SourceIP=' + lineSRC + ' bytes=' + lineBytes + ' ' + str(int(lineDate.timestamp()))
  
  return(parsedLine)

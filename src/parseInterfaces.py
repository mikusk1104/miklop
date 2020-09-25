import json, dateParser, re
from datetime import datetime

def parseInterface(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''
  
  line = lineParsedLine["msg"]
  lineHostName = line[1:line.find(": ")]
  lineParsedMsg = line.split(";")

  for x in lineParsedMsg:
    if "name" in x:
      lineIntName = x[x.find("=")+1:]
    if "rx-bits-per-second" in x:
      lineRXbits = x[x.find("=")+1:]
    if "tx-bits-per-second" in x:
      lineTXbits = x[x.find("=")+1:]
    if "rx-drops-per-second" in x:
      lineRXdrops = x[x.find("=")+1:]
    if "rx-errors-per-second" in x:
      lineRXerrors = x[x.find("=")+1:]
    if "tx-drops-per-second" in x:
      lineTXdrops = x[x.find("=")+1:]
    if "tx-errors-per-second" in x:
      lineTXerrors = x[x.find("=")+1:]

  parsedLine = lineHostName + '_INTERFACES' + ',Interface=' + lineIntName + ' RX=' + lineRXbits + ',TX=' + lineTXbits + ',RXDrops=' + lineRXdrops + ',TXDrops=' + lineTXdrops + ',RXError=' + lineRXerrors + ',TXError=' + lineTXerrors + ' ' + str(int(lineDate.timestamp()))

  return(parsedLine)

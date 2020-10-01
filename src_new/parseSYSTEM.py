import json
import dateParser
from datetime import datetime

def parseSystem(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''

  lineParsedMsg = lineParsedLine["msg"].split()

  lineHostName = lineParsedMsg[0][:-1]
  lineCPULoad = lineParsedMsg[2][8:]
  lineFreeMEM = lineParsedMsg[3][8:]
  lineTotalMEM = lineParsedMsg[4][9:]
  lineFreeHDD = lineParsedMsg[5][8:]
  lineTotalHDD = lineParsedMsg[6][9:]

  parsedLine = lineHostName + '_SYSTEM' + ' CPULoad=' + lineCPULoad + ',FreeMEM=' + lineFreeMEM + ',TotalMEM=' + lineTotalMEM + ',FreeHDD=' + lineFreeHDD + ',TotalHDD=' + lineTotalHDD + ' ' + str(int(lineDate.timestamp()))
  
  return(parsedLine)
  
import json
import dateParser

from datetime import datetime

def parseUserLogged(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''

  lineParsedMsg = lineParsedLine["msg"].strip()
  lineParsedMsg = lineParsedMsg.split()
  
  lineHostName = lineParsedMsg[0][:-1]
  lineUserName = lineParsedMsg[2]
  lineAction = lineParsedMsg[4]
  lineIP = lineParsedMsg[6]
  lineVIA = lineParsedMsg[8]

  parsedLine = lineHostName + '_USERS' + ',Action=logged_' + lineAction + ',UserName=' + lineUserName + ',Via=' + lineVIA + ',IP=' + lineIP + ' value=1 ' + str(int(lineDate.timestamp()))

  return(parsedLine)

def parseUserLoginFailure(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''

  lineParsedMsg = lineParsedLine["msg"].strip().split()

  lineHostName = lineParsedMsg[0][:-1]
  lineUserName = lineParsedMsg[5]
  lineIP = lineParsedMsg[7]
  lineVIA = lineParsedMsg[9]

  parsedLine = lineHostName + '_USERS' + ',Action=login_failure' + ',UserName=' + lineUserName + ',Via=' + lineVIA + ',IP=' + lineIP + ' value=1 ' + str(int(lineDate.timestamp()))

  return(parsedLine)

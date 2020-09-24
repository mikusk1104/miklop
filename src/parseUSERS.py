import json, dateParser, re
from datetime import datetime

def parseUserLogged(message, lastTime):
  lineParsedLine = json.loads(message)
  lineDate = dateParser.dateParser(lineParsedLine['time'])
    
  if lineDate < lastTime:
    return ''

  lineParsedMsg = lineParsedLine["msg"].split()

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

  lineParsedMsg = lineParsedLine["msg"]
  lineParsedMsg = lineParsedMsg[1:]

  lineHostName = lineParsedMsg[0:lineParsedMsg.find(":")].replace(" ", "_")
  lineUserName = lineParsedMsg[lineParsedMsg.find("user")+len("user "):lineParsedMsg.find(" from")].replace(" ","_")
  lineIP = lineParsedMsg[lineParsedMsg.find("from")+len("from "):lineParsedMsg.find(" via")].replace(" ","_")
  lineVIA = lineParsedMsg[lineParsedMsg.find("via")+len("via "):].replace(" ","_")
  
  parsedLine = lineHostName + '_USERS' + ',Action=login_failure' + ',UserName=' + lineUserName + ',Via=' + lineVIA + ',IP=' + lineIP + ' value=1 ' + str(int(lineDate.timestamp()))

  return(parsedLine)

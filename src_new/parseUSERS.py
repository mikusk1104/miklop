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
  
  i = 0
  while i < len(lineParsedMsg):
    print(lineParsedMsg[i])
    if ':' in lineParsedMsg[i]:
      lineHostName = lineParsedMsg[i][:-1]
      if lineHostName == '':
        return ''

    if 'user' in lineParsedMsg[i]:
      lineUserName = lineParsedMsg[i+1]
      if lineHostName == '':
        return ''

    if 'logged' in lineParsedMsg[i]:
      lineAction = lineParsedMsg[i+1]
      if lineAction == '':
        return ''
    
    if 'from' in lineParsedMsg[i]:
      lineIP = lineParsedMsg[i+1]
      if lineIP == '':
        return ''

    if 'via' in lineParsedMsg[i]:
      lineVIA = lineParsedMsg[i+1]
      if lineVIA == '':
        return ''

    i = i + 1

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

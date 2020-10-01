import json

message = '{"time":"2020-10-01T03:20:08.372731+00:00","syslogtag":"system,error,critical","msg":" router.k: login failure for user mikusk from 192.168.27.195 via winbox"}'

lineParsedLine = json.loads(message)
lineParsedMsg = lineParsedLine["msg"].strip().split()


print(lineParsedMsg)

lineHostName = lineParsedMsg[0][:-1]
lineUserName = lineParsedMsg[5]
lineIP = lineParsedMsg[7]
lineVIA = lineParsedMsg[9]

parsedLine = lineHostName + '_USERS' + ',Action=login_failure' + ',UserName=' + lineUserName + ',Via=' + lineVIA + ',IP=' + lineIP + ' value=1 '

print(parsedLine)
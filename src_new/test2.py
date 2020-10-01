import json

message = '{"time":"2020-10-01T19:18:24.361322+00:00","syslogtag":"script,info","msg":" router.k: .id=*0;bytes=78;dst-address=192.168.26.183;packets=1;src-address=142.250.27.188;script=accounting"}'

lineParsedLine = json.loads(message)
lineParsedMsg = lineParsedLine["msg"].strip().split(';')


print(lineParsedMsg)

lineHostName = lineParsedMsg[0][:lineParsedMsg[0].find(": ")]
lineDST = lineParsedMsg[2][12:]
lineSRC = lineParsedMsg[4][12:]
lineBytes = lineParsedMsg[1][6:]

parsedLine = lineHostName + '_accounting' + ',DestinationIP=' + lineDST + ',SourceIP=' + lineSRC + ' bytes=' + lineBytes

print(parsedLine)
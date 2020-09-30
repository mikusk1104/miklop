import json

message = '{"time":"2020-09-30T02:00:16.998144+00:00","syslogtag":"router.k:","msg":" query from 192.168.99.11: #31458 gggg.wwww.mikrotik.com. A"}'

lineParsedLine = json.loads(message)

print(lineParsedLine)

time = lineParsedLine['time']
hostname = lineHostName = lineParsedLine["syslogtag"][:-1]
lineParsedMsg = lineParsedLine["msg"].split()
lineParsedDomain = lineParsedMsg[4][:-1].split('.')

domainLenght = len(lineParsedDomain)

domain = lineParsedDomain[domainLenght-2] + '.' + lineParsedDomain[domainLenght-1]


print(time, hostname, lineParsedMsg, lineParsedDomain, domainLenght, domain)
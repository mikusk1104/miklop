import sys, getConfig, dateParser, datetime, parseDNS, writeInfluxDB, time
from collections import Counter
while True:
  configFile = getConfig.getConfigFile(sys.argv[1:])

  config = getConfig.getConfig(configFile)
  logFile = config['logfile'][1:-1]
  lastTimeStrUTC = config['lasttimeutc']
  lastTimeObj = dateParser.dateParser(lastTimeStrUTC[1:-1])
  
  time.sleep(60)
  sys.stdout.write(configFile)
  sys.stdout.write(logFile)
  sys.stdout.write(lastTimeObj)

  f = open(logFile)
  line = f.readline()
  parsedLine = []
 
  while line:
    if "query from" in line:
      t = parseDNS.parseDNS(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)
    if "script=dns" in line:
      t = parseDNS.parseDNS_cache(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)
    line = f.readline()    
  f.close()
  sys.stdout.write(parsedLine)    
  writeInfluxDB.writeInfluxDB(parsedLine)
  getConfig.writeLastTime(configFile)


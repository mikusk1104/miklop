import sys, datetime, time, logging
import getConfig, dateParser, parseDNS, writeInfluxDB, parseUSERS, parseSYSTEM, parseInterfaces, parseAccounting
import logging.handlers as handlers
from collections import Counter

configFile = getConfig.getConfigFile(sys.argv[1:])
config = getConfig.getConfig(configFile)
logFile = config['logfile'][1:-1]
appLogFile = config['applogfile'][1:-1]
lastTimeStrUTC = config['lasttimeutc']
lastTimeObj = dateParser.dateParser(lastTimeStrUTC[1:-1])

logger = logging.getLogger('miklop')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='"%Y-%m-%dT%H:%M:%S %z"')
logHandler = handlers.RotatingFileHandler(appLogFile, maxBytes=5000000, backupCount=5)
logHandler.setLevel(logging.INFO)
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
  
sys.stdout.write(configFile + '\n')
sys.stdout.write(logFile + '\n')
sys.stdout.write(appLogFile + '\n')
sys.stdout.write(str(lastTimeObj) + '\n')

logger.info('Trying open file: ' + logFile)
f = open(logFile)
line = f.readline()
parsedLine = []

while True:
  while line:
    if "query from" in line:
      t = parseDNS.parseDNS(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)
    
    if "script=dns" in line:
      t = parseDNS.parseDNS_cache(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)
    
    if "logged in" in line or "logged out" in line:
      t = parseUSERS.parseUserLogged(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)

    if "login failure" in line:
      t = parseUSERS.parseUserLoginFailure(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)

    if "script=system" in line:
      t = parseSYSTEM.parseSystem(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)

    if "rx-bits-per-second=" in line:
      t = parseInterfaces.parseInterface(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)

    if "script=accounting" in line:
      t = parseAccounting.parseAccounting(line, lastTimeObj)
      if t != '':
        parsedLine.append(t)

    line = f.readline()    
  
  f.close()
  
#  sys.stdout.write(str(parsedLine) + '\n')    
  
#  writeInfluxDB.writeInfluxDB(parsedLine)
  
#  getConfig.writeLastTime(configFile)
  
  time.sleep(60)

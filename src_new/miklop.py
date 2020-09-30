import getConfig

import sys
import logging
import logging.handlers as handlers

sys.stdout.write('Getting config file \n')
try:
  configFile = getConfig.getConfigFile(sys.argv[1:])
except:
  sys.stdout.write('Please start program with parameter -c <config file> \n')
  sys.stdout.write('Example: python miklop.py -c config.ini \n')
  sys.stdout.write('exiting ... \n')
  exit()

sys.stdout.write('Config file = ' + configFile + '\n')

sys.stdout.write('Getting config items from file \n')
try:
  config = getConfig.getConfig(configFile)
except:
  sys.stdout.write('Config file does not exist or wrong format, exiting ... \n')
  exit()

logFile = config['logfile'][1:-1]
appLogFile = config['applogfile'][1:-1]
lastTimeStrUTC = config['lasttimeutc']

sys.stdout.write('Log file: ' + logFile + '\n')
sys.stdout.write('Application log file: ' + appLogFile + '\n')
sys.stdout.write('Last time: ' + lastTimeStrUTC + '\n')

sys.stdout.write('Activating logging to file: ' + logFile + '\n')
try:
  logger = logging.getLogger('miklop')
  logger.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='"%Y-%m-%dT%H:%M:%S %z"')
  logHandler = handlers.RotatingFileHandler(appLogFile, maxBytes=5000000, backupCount=5)
  logHandler.setLevel(logging.INFO)
  logHandler.setFormatter(formatter)
  logger.addHandler(logHandler)
except:
  sys.stdout.write('Problem activating logging to file \n')
  sys.stdout.write('Please Check if correct file is specified in ' +  configFile + ' in section "applogfile" \n')
  sys.stdout.write('exiting ... \n')
  exit()
sys.stdout.write('Switching from STDOUT to application logging please check this file: ' + logFile + '\n')


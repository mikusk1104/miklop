import logging
import logging.handlers as handlers

try:
  logger = logging.getLogger('miklop')
  logger.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='"%Y-%m-%dT%H:%M:%S %z"')
  logHandler = handlers.RotatingFileHandler('test.log', maxBytes=5000000, backupCount=5)
  logHandler.setLevel(logging.INFO)
  logHandler.setFormatter(formatter)
  logger.addHandler(logHandler)
except:
  print('problem setup logging components, exiting ... ')
  exit()

logger.info('Setup logging components done.')





# try:
#   1/0
# except:
#   logging.exception("message")
# finally:
#   print('hotovo')


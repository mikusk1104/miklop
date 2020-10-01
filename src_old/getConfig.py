import argparse
from configparser import ConfigParser
from datetime import datetime
from pytz import timezone


def getConfigFile(arguments):
  parser = argparse.ArgumentParser(description="This program export Mikrotik measurements into TMDBs")
  parser.add_argument("-c", "--configFile", required=True, help="path to config file")
  args = parser.parse_args(arguments)
  return args.configFile

def getConfig(configFile):
  config = ConfigParser()
  config.read(configFile)
  return dict(config.items("MAIN"))

def writeLastTime(configFile):
  now_utc = datetime.now(timezone('UTC')).isoformat()
  
  config = ConfigParser()
  config.read(configFile)

  config.set("MAIN", "lasttimeutc", '"' + now_utc + '"')

  cfgfile = open(configFile ,'w')
  config.write(cfgfile)
  cfgfile.close()

def FileCheck(fn):
  try:
    open(fn, "r")
    return 1
  except IOError:
    return 0

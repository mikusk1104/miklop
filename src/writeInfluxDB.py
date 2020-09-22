from influxdb import InfluxDBClient

def writeInfluxDB(parsedLine):
  client = InfluxDBClient(host='pi.k', port=8086)
  client.write_points(parsedLine, database='mikrotik', time_precision='s', batch_size=10000, protocol='line')

from influxdb import InfluxDBClient

def writeInfluxDB(parsedLine, influx_hostname, influx_port, influx_db):
  client = InfluxDBClient(host=influx_hostname, port=influx_port)
  client.write_points(parsedLine, database=influx_db, time_precision='s', batch_size=10000, protocol='line')

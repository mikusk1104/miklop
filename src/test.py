line = " router.k: .id=*3;comment=internet;fp-rx-bits-per-second=30864656;fp-rx-packets-per-second=2554;fp-tx-bits-per-second=624784;fp-tx-packets-per-second=1385;name=ether1;rx-bits-per-second=30934240;rx-drops-per-second=0;rx-errors-per-second=0;rx-packets-per-second=2553;tx-bits-per-second=723248;tx-drops-per-second=0;tx-errors-per-second=0;tx-packets-per-second=1385;tx-queue-drops-per-second=0"
line =  line[1:]

lineHostName = line[:line.find(": ")]

lineParsedMsg = line.split(";")

for x in lineParsedMsg:
  if "name" in x:
    lineIntName = x[x.find("=")+1:]
  if "rx-bits-per-second" in x:
    lineRXbits = x[x.find("=")+1:]
  if "tx-bits-per-second" in x:
    lineTXbits = x[x.find("=")+1:]
  if "rx-drops-per-second" in x:
    lineRXdrops = x[x.find("=")+1:]
  if "rx-errors-per-second" in x:
    lineRXerrors = x[x.find("=")+1:]
  if "tx-drops-per-second" in x:
    lineTXdrops = x[x.find("=")+1:]
  if "tx-errors-per-second" in x:
    lineTXerrors = x[x.find("=")+1:]

parsedLine = lineHostName + '_INTERFACES' + ',Interface=' + lineIntName + ' RX=' + lineRXbits + ',TX=' + lineTXbits + ',RXDrops=' + lineRXdrops + ',TXDrops=' + lineTXdrops + ',RXError=' + lineRXerrors + ',TXError=' + lineTXerrors

print(parsedLine)
line = " router.k: .id=*0;bytes=7277;dst-address=192.168.28.191;packets=13;src-address=52.17.157.213;script=accounting"
line =  line[1:]

lineHostName = line[:line.find(": ")]

lineParsedMsg = line.split(";")

for x in lineParsedMsg:
  if "bytes" in x:
    lineBytes = x[x.find("=")+1:]
  if "dst-address" in x:
    lineDST = x[x.find("=")+1:]
  if "src-address" in x:
    lineSRC = x[x.find("=")+1:]
  
parsedLine = lineHostName + '_accounting' + ',DestinationIP=' + lineDST + ',SourceIP=' + lineSRC + ' bytes=' + lineBytes

print(parsedLine)
line = " router.k: script=system cpuLoad=0 freeMEM=77639680 totalMEM=134217728 freeHDD=1794048 totalHDD=15990784"
line =  line[1:]

lineParsedMsg = line.split()
    
lineHostName = lineParsedMsg[0][:-1]
lineCPULoad = lineParsedMsg[2][8:]
lineFreeMEM = lineParsedMsg[3][8:]
lineTotalMEM = lineParsedMsg[4][9:]
lineFreeHDD = lineParsedMsg[5][8:]
lineTotalHDD = lineParsedMsg[6][9:]

parsedLine = lineHostName + '_SYSTEM' + ' CPULoad=' + lineCPULoad + ',FreeMEM=' + lineFreeMEM + ',TotalMEM=' + lineTotalMEM + ',FreeHDD=' + lineFreeHDD + ',TotalHDD=' + lineTotalHDD + ' ff'

print(parsedLine)
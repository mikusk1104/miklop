line = " router.k: login failure for user mikusk kubo from 192.168.27.195 via winbox"
line =  line[1:]

hostname = line[0:line.find(":")]
user = line[line.find("user")+len("user "):line.find(" from")]
ip = line[line.find("from")+len("from "):line.find(" via")]
action = "login failure"
via = line[line.find("via")+len("via "):]
print(line)
print(hostname,user,ip,via)

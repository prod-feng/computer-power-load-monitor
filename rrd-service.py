#!/usr/bin/python3

import time
import rrdtool
import subprocess

def updateRRD(rrd, start,LOADPCT,load,mem):
   #print('Update: ',start,LOADPCT,load,mem)
   rrdtool.update(rrd,'%s:%s:%s:%s'%(start,LOADPCT,load,mem))


# Open the existing RRD file
rrd='/home/feng/rrd/power-metrics.rrd'


# Repeat forever
while (True):

   # Collect data per 10 seconds(depending on the setting of the rrd file when create).
   output2 = subprocess.getoutput("apcaccess -p LOADPCT|awk '{print $1}';uptime |awk '{print $11}'|tr ',' ' ';free -g|grep Mem|awk '{print $3}'")
   start = int(time.time())
   power,load,memused=output2.split()
   LOADPCT=int(8.65*float(power))
   loadint=int(float(load))
   memusedint=int(memused)
   #print("haha", output,start,LOADPCT,' '.join(output2.split('\n')))
   time.sleep(10)
   # Update the RRD file
   updateRRD(rrd, start,LOADPCT, loadint, memusedint)

#!/usr/bin/python3

import time
import rrdtool
import subprocess

#creat rrd file
rrd='/home/feng/rrd/power-all.rrd'

rrdtool.create(rrd,
               '--step', '10',
               'DS:power:GAUGE:20:0:U',
               'DS:load:GAUGE:20:0:100',
               'DS:memused:GAUGE:20:0:900',
               'RRA:MAX:0.5:1:864000',
               'RRA:MAX:0.5:1:864000',
               'RRA:MAX:0.5:1:864000',)

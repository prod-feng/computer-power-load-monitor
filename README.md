# computer-power-load-monitor

A simple Python script to monitor APC power usage, and cpu load, memory used. Only use simple command lines, set a user namespace service to run. Ubuntu 22.

1. Install apcupsd package.
 ```
   sudo apt  install apcupsd
```
2. set up user space service.

You can hen use "rrdtool graph  ..." to read and generate a graph of these metrics.
   

import re
from decimal import Decimal

alert = """
threshold of Free Swap not met: current value 0.000000
"""

m = re.search('(threshold of )(\S+)(.*)(current value )(\d[\.]?[\d]*)', alert)
if m:
	process = m.group(2)
	process2 = m.group(3)
	value = int(round(Decimal(m.group(5))))
	print process
	print process2
	print value
if "Free_Swap" in process:
	alert2 = "Swap: %s%% used." % (value)
	print alert2

#print process
#print value

#if alert.startswith('threshold of Free Swap'):
#	m = re.search("current value ([\d]+)", evt.summary)
#	if m:
#		currentload = float(m.group(1)) / 100
#		evt.summary = "High Load: %s" % (currentload)
#		evt.message = evt.summary
#if "High_Heap_JT" in process:
#	alert2 = "Job Tracker Heap: %s%% user." % (value)
#elif "HBase" in process:
#	alert2 = "High HBase Regions: %s used." % (value)
#else:
#	alert2 = "%s alert: %s%% used." % (process, value)

#print alert2


#if "GWC_Processes_Logging" in process:
#				 evt.summary = "Gateway Controller process is not responding"
# elif "PCL_Proccesses_Logging" in process:
#				  evt.summary = "PCL Endpoint process is not responding"

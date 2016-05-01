import re
from decimal import Decimal

alert = """
threshold of HBase Regions Warning exceeded: current value 215.000000
"""

m = re.search('(threshold of )(\S*)(.*)(current value )(\d[\.]?[\d]*)', alert)
if m:
	process = m.group(2)
	value = int(round(Decimal(m.group(5))))

if "High_Heap_JT" in process:
	alert2 = "Job Tracker Heap: %s%% user." % (value)
elif "HBase" in process:
	alert2 = "High HBase Regions: %s used." % (value)
else:
	alert2 = "%s alert: %s%% used." % (process, value)

print alert2


#if "GWC_Processes_Logging" in process:
#				 evt.summary = "Gateway Controller process is not responding"
# elif "PCL_Proccesses_Logging" in process:
#				  evt.summary = "PCL Endpoint process is not responding"

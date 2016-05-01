import re
from decimal import Decimal

alert = """
threshold of HDFS_Used_Error not met: current value 78.000000
"""

m = re.search('(threshold of )(\S*)(.*)(current value )(\d[\.]?[\d]*)', alert)
if m:
	process = m.group(2)
	value = int(round(Decimal(m.group(5))))

if "HDFS_Used" in process:
	alert2 = "HDFS: %i%% used." % (100-value)

print alert2


#if "GWC_Processes_Logging" in process:
#				 evt.summary = "Gateway Controller process is not responding"
# elif "PCL_Proccesses_Logging" in process:
#				  evt.summary = "PCL Endpoint process is not responding"

import re
import string
from decimal import Decimal

m = re.search('(threshold of )(\S*)(.*)(current value )(\d[\.]?[\d]*)', evt.summary)
if m:
	 process = m.group(2)
	  value = int(round(Decimal(m.group(5))))

	  if evt.summary.startswith('threshold of high load'):
		   if evt.severity == 0:
			     evt.summary = "HDFS usage has fallen below the warning threshold of 65%"
			       evt.message = evt.summary
			        else:
					  evt.summary = "HDFS: %i%% used" % (100-value)
					    evt.message = "%s. \nPlease check http://namenode.explorys:50070/dfshealth.jsp" % (evt.summary)
				    elif "HDFS_Usage_Critical" in process:
					     if evt.severity == 0:
						       evt.summary = "HDFS usage has fallen below the critical threshold of 70%"
						         evt.message = evt.summary
							  else:
								    evt.summary = "HDFS: %i%% used" % (100-value)
								      evt.message = "%s. \nPlease check http://namenode.explorys:50070/dfshealth.jsp" % (evt.summary)

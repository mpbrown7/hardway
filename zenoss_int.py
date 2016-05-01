import re
  
if device:
  fs_id = device.prepId(evt.component)
  for f in device.os.interfaces():
     if f.id != fs_id: continue
  
     # Extract the percent and utilization from the summary
     m = re.search("threshold of [^:]+: current value ([\d\.]+)", evt.message)
     if not m: continue
     currentusage = (float(m.groups()[0])) * 8
  
     if f.speed != 0:
         p = (currentusage / f.speed) * 100
     else:
         p = (currentusage / 1000000000) * 100
     
     evtKey = evt.eventKey
  
     # Whether Input or Output Traffic
     if evtKey == "ifHCInOctets_ifHCInOctets|high utilization":
         evtNewKey = "In"
     elif evtKey == "ifHCOutOctets_ifHCOutOctets|high utilization": 
        evtNewKey = "Out"
     else:
         evtNewKey = "In or Out"
  
     # Check the speed to determine the appropriate conversion
     # 10Gbps utilization
     if currentusage > 10000000000:
         Usage = currentusage / 10000000000
         evt.summary = "Network: %3.2f Gbps %s (%3.2f%%) - %s" %  (Usage, evtNewKey, p, f.description)
         evt.message = evt.summary
  
     # Gbps utilization
     elif currentusage > 1000000000:
         Usage = currentusage / 1000000000
         evt.summary = "Network: %3.2f Gbps %s (%3.2f%%) - %s" %  (Usage, evtNewKey, p, f.description)
         evt.message = evt.summary
  
     # Mbps utilization
     elif currentusage > 1000000:
         Usage = currentusage / 1000000
         evt.summary = "Network: %3.2f Mbps %s (%3.2f%%) - %s" %  (Usage, evtNewKey, p, f.description)
         evt.message = evt.summary
  
     # Kbps utilization
     elif currentusage > 1000:
         Usage = currentusage / 1000
         evt.summary = "Network: %3.2f Kbps %s (%3.2f%%) - %s" %  (Usage, evtNewKey, p, f.description)
         evt.message = evt.summary
  
     # bps  utilization
     elif currentusage < 1000:
         Usage = currentusage
         evt.summary = "Network: %3.2f bps %s (%3.2f%%) - %s" %  (Usage, evtNewKey, p, f.description)
         evt.message = evt.summary
  
     break
  

import urllib,sys
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET
from exceptions import Exception

if rtcServer is None:
  print "No RTC server provided."
  sys.exit(1)

# Check we have a project set somewhere (can be over-ridden or set Server level)
if rtcProject is None:
  if rtcServer['rtcProject'] is None:
    print "No RTC Project provided"
    sys.exit(1)
  else:
    rtcProject = rtcServer['rtcProject']

rtcURL = rtcServer['url']
if rtcURL.endswith('/'):
  rtcURL = rtcURL[:len(rtcURL)-1]

request = HttpRequest(rtcServer, username, password)

# Now we want to perform an update of our work item - specifically to change the workitem status
headers = {'Content-type': 'application/x-oslc-cm-change-request+json', 'Accept' : 'application/x-oslc-cm-change-request+json'}
#context = workItemURL[len(rtcURL):]
context = "resource/itemName/com.ibm.team.workitem.WorkItem/" + workItemID

resp = request.get( context , headers=headers)
print resp.response

commentJSON = '{ "dc:description": updateComment }'
context += "/rtc_cm:comments"
print "Context is " + context
resp = request.post( context , body=commentJSON, headers=headers)

if resp.isSuccessful:
  print resp.response
else:
  print "Something went wrong - stone the crows"
  sys.exit(1)




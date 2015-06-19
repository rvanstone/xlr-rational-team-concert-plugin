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

# Form the request
request = HttpRequest(rtcServer, username, password)

# We want to perform an update of our work item - specifically to change the workitem status
headers = {'Content-type': 'application/x-oslc-cm-change-request+json', 'Accept' : 'application/x-oslc-cm-change-request+json'}
context = "resource/itemName/com.ibm.team.workitem.WorkItem/" + workItemID 

# Get the workitem we have been chosen
resp = request.get( context , headers=headers)
if resp.isSuccessful:
  print "Found our workitem"
else:
  print "Something went wrong"
  print resp.errorDump()
  sys.exit(1)
  

# Now update the state of the workitem
# You can not update the state directly with a body element you have to invoke an RTC action.
# RTC Actions are part of the workflow defined for the workitems (Defects, Tasks etc)
# Different workitem types have different workflows and therefore different actions
# As a consequence depending on your set up, you may not be able to move from your current state to the desired state
# This is a big TODO in this plugin
# Determine the available states
# Determine if you can move from current to desired
# Throw error if this is not possible (or silently fail)
# Or progress through the workflow...
# The comment added here is in fact a description - more work required to add comments to a task
################
states = {"Done":"com.ibm.team.workitem.taskWorkflow.action.resolve",
          "InProgress":"com.ibm.team.workitem.taskWorkflow.action.startWorking"}

commentString = updateComment + " State changed to " + newState
body = '{ "dc:description" : "' + commentString + '"}'

statusContext = context + "/rtc_cm:comments?_action=" + states[newState]
print statusContext

resp = request.put( statusContext, body=body ,headers=headers )
if resp.isSuccessful:
  print resp.response
else:
  print "Something went wrong"
  sys.exit(1)
  print resp.errorDump()



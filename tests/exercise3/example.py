from genie.conf import Genie
from genie.utils import Dq
from genie.testbed import load
import json

tb = load('../../testbed/sandbox-devices.yaml')       # Load our testbed file from a file.
dev = tb.devices['internet-rtr01']       # Define an object called dev from the device named csr1000v

dev.connect()      # Connect to the object dev we defined earlier -  this must be done before parsing to the device

routingTable = dev.parse('show ip route')        # Run the command "show ip route" on the device and parse the output to JSON

routes = len(routingTable['vrf']['default']['address_family']['ipv4']['routes']) # Work out how many routes are in the routing table by working out the length of the routes list from the datastructure returned by pyATS

if routes == 5:
   print("Pass: The expected number of routes are in the oruting table")
elif routes < 5:
   print("Fail: There are less routes in the routing table than expected")
elif routes > 5:
   print("Fail: There are more routes in the routing table than expected")

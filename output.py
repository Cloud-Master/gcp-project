from terrascript import *
from terrascript.google.r import *
from variables import *
from vm import *

ts = Terrascript()

ts += output('public_ip', value='inst.network_interface.0.access_config.0.nat_ip')

print(ts.dump())
file = open("./terraform/output.tf.json", "w")
file.write(ts.dump())
file.close()

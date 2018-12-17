from terrascript import Terrascript, provider
from terrascript.google.r import *
ts = Terrascript()
## Add Resources to Terraform files
nw = ts.add(
            google_compute_network(
                'test-network',
                name='test-pavan-nw',
                auto_create_subnetworks = True))
#print(nw.name)

file = open("./terraform/nw.tf.json", "w")
file.write(ts.dump())
file.close()

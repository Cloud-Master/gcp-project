from terrascript import Terrascript, provider
from terrascript.google.r import *
from variables import *
ts = Terrascript()
## Add Resources to Terraform files
nw = ts.add(
            google_compute_network(
                'test-network',
                name='test-pavan-nw',
                auto_create_subnetworks = False,
                routing_mode = 'GLOBAL'))

snw = ts.add(
    google_compute_subnetwork(
        'test-snw',
        name = 'test-pavan-snw',
        ip_cidr_range = '10.5.0.0/16',
        region = region,
        network = nw.name
    )
)
#print(nw.name)

file = open("./terraform/nw.tf.json", "w")
file.write(ts.dump())
file.close()

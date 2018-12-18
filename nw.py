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

firewall80 = ts.add(
    google_compute_firewall(
        'test-firewall',
        name = 'test-pavan-80',
        network = nw.name,
        allow = [{'protocol': 'tcp', 'ports':[{'80', '443'}]}],
        source_ranges = ['0.0.0.0/0'],
        target_tags = ['test-http']
    )
)

firewall22 = ts.add(
    google_compute_firewall(
        'test-firewall',
        name = 'test-pavan-22',
        network = nw.name,
        allow = [{'protocol': 'ssh', 'ports':[{'22'}]}],
        source_ranges = ['0.0.0.0/0'],
        target_tags = ['test-ssh']
    )
)
#print(nw.name)

file = open("./terraform/nw.tf.json", "w")
file.write(ts.dump())
file.close()

from terrascript import Terrascript, provider
from terrascript.google.r import *
from nw import *
from variables import *
ts = Terrascript()



ts.add(
        google_compute_instance(
            'test-vm', 
            name='test-pavan-tft', 
            boot_disk=[{'initialize_params':[{'image':'debian-cloud/debian-9'}]}], 
            network_interface=[{'subnetwork': snw.self_link, 'access_config':{} }],
            machine_type='n1-standard-1', 
            zone=zone,
            metadata_startup_script = '${data.start_up.startup_script.rendered}'
        ))

file = open("./terraform/vm.tf.json", "w")
file.write(ts.dump())
file.close()

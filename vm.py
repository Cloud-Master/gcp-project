from terrascript import Terrascript, provider
from terrascript.google.r import *
from nw import *
ts = Terrascript()

ts.add(
        google_compute_instance(
            'test-vm', 
            name='test-pavan-tft', 
            boot_disk=[{'initialize_params':[{'image':'debian-cloud/debian-9'}]}], 
            network_interface=[{'network': nw.name, 'access_config':{} }],
            machine_type='n1-standard-1', 
            zone='us-central1-b'))

file = open("./terraform/create-vm.tf.json", "w")
file.write(ts.dump())
file.close()

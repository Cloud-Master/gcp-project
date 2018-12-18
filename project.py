# Module to initialize Terraform to launch infrastructure on Google
from python_terraform import *

import provider 
import vm
import nw
### Generate Terraform files with Terrascript Module
## Terrascript object Creation

tf = Terraform(working_dir='./terraform')

# tf.init()
# approve = {"auto-approve": True}
# print(tf.plan())
# print(tf.apply(**approve))

#print(tf.apply())
#output('example_public_ip', value=example.public_ip, description='Public IP of example')

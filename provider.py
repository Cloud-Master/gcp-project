# Module to generate Terraform files to launch infrastructure on Google
from terrascript import Terrascript, provider
from terrascript.google.r import *
### Generate Terraform files with Terrascript Module
## Terrascript object Creation
ts = Terrascript()
## Add provider to Terraform files.
ts += provider('google', credentials='../service_account.json', project='learn-internal', region='us-central1')

print(ts.dump())
file = open("./terraform/provider.tf.json", "w")
file.write(ts.dump())
file.close()


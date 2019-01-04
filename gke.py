from terrascript import Terrascript, provider
from terrascript.google.r import *
from python_terraform import *

ts = Terrascript()
region='asia-south1'
ts += provider('google', credentials='../service_account_gke.json', project='learn-internal', region= region)

nw = ts.add(
            google_compute_network(
            'test-network',
            name='test-gke-nw',
            auto_create_subnetworks = False,
            routing_mode = 'GLOBAL'))

snw = ts.add(
             google_compute_subnetwork(
             'test-snw',
             name = 'test-gke-snw',
             ip_cidr_range = '10.5.0.0/16',
             region = region,
             network = nw.name))

gke = ts.add(
            google_container_cluster(
            'primary',
            name='my-cluster',
            zone='asia-south1-a',
            additional_zones=['asia-south1-b','asia-south1-c'],
            cluster_ipv4_cidr='172.16.0.0/16',
            network = nw.name,
            subnetwork = snw.name,
            master_auth=[{'username': 'test', 'password': 'test123456789012'}],
            initial_node_count ='2'))

file = open("./terraform/create-gke.tf.json", "w")
file.write(ts.dump())
file.close()
tf = Terraform(working_dir='./terraform')
tf.init()
approve = {"auto-approve": True}
print(tf.plan())
print(tf.apply(**approve))
print(tf.apply())
print(gke)

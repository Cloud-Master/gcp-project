from terrascript import *
# from sys import *
#
# with open("variables", 'r') as ft:
#     txt = ft.read()
# print(txt)
# myvars = {}
# with open("variables") as myfile:
#     for line in myfile:
#         name, var = line.partition("=")[::2]
#         myvars[name.strip()] = str(var)
# var_project = myvars["project"]
#print("The given Project is :", var_project)

project = variable('project')
region = variable('region')
zone = variable('zone')

ts = Terrascript()
ts += variable('project')
ts += variable('region')
ts += variable('zone')


# ts += data('start_up', name = "startup_script", template = "${file(./files/start_up.sh)}")

#aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})

print(zone)
print(ts.dump())

file = open("./terraform/variables.tf.json", "w")
file.write(ts.dump())
file.close()
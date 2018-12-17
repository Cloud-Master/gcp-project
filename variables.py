from terrascript import provider, dump, variable
from sys import *
#
# with open("variables", 'r') as ft:
#     txt = ft.read()
# print(txt)
# myvars = {}
# with open("variables") as myfile:
#     for line in myfile:
#         name, var = line.partition("=")[::2]
#         myvars[name.strip()] = str(var)
#
#
# var_project = myvars["project"]
#print("The given Project is :", var_project)

var_project = variable('learn-internal')
var_region = variable('region', default='us-central1')
var_zone = variable('zone')

#aws_amis = variable('aws_amis', default={'us-east-1': 'ami-5f709f34', 'us-west-2': 'ami-7f675e4f'})

print(var_region)
print(var_project)

print(dump())
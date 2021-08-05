import logging
import json
import os
from ipaddress import ip_address, ip_network
from config import TheHive
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CustomFieldHelper
from thehive4py.query import *

def __repr__(self):
    return str(self.__dict__)
                           
thapi = TheHiveApi(TheHive.get('url', None),
   TheHive.get('key'),
   TheHive.get('password', None),
   TheHive.get('proxies'),
   TheHive.get('verify'))

#tags = []
#tags.append('src:inthreat.com')
#query = In('tags', tags)
# print(str(query))

query = Eq("customFields.offenseSource.string", "QRadar_Offenses")
response = thapi.find_cases(query=query)
for returned_case in response.json():
    case_id = returned_case['_id']
    print(case_id)
    obs_response = thapi.get_case_observables(case_id)
    for returned_observable in obs_response.json():
        if returned_observable['dataType'] == "ip":
            print(returned_observable['data'])
            if ip_address(returned_observable['data']) in ip_network('192.168.0.0/16') or ip_address(returned_observable['data']) in ip_network('10.0.0.0/8') or ip_address(returned_observable['data']) in ip_network('192.195.100.0/25'):
                print("local address")
        if returned_observable['dataType'] == "domain":
            print(returned_observable['data'])

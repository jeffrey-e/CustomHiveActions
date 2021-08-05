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

query = dict()
query['case'] = "nOi6wHEBMjz6HV7K1u5n"
response = thapi.find_alerts(query=query)
print(response.json())

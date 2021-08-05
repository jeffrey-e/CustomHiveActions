import logging
import json
import os
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

query = Eq('status', "New")
# print(str(query))
response = thapi.find_alerts(query=query)
#print(response.text)
for returned_alert in response.json():
    #print("Found {}".format(returned_alert))
    alert_id = returned_alert['id']
    print ("Alert ID: {}, Title: {}".format(returned_alert['id'], returned_alert['title']))
    print("Importing Alert...")
    response = thapi.create_case_from_alert(alert_id, returned_alert['caseTemplate'])
    print(json.loads(response.text))
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

tags = []
tags.append('ELK')
query = In('tags', tags)

#query = Eq('source', 'MISP-extern')
#alertNew = Eq('status', 'New')
#query = And(sourceMISP, alertNew)

# print(str(query))
response = thapi.find_alerts(query=query)
print(json.loads(response.text))

for returned_alert in response.json():
    print(returned_alert)
    #if 'summary' in case:
    #    print(case['summary'])
    if returned_alert['status'] == "New":
        print(("Found {} with id: {}".format(returned_alert['title'].encode("utf-8"),returned_alert['id'].encode("utf-8"))))
        #Grab alertid
        alertid = returned_alert['id'].encode("utf-8")
        # Place actual request
        response = thapi.mark_alert_as_read(alertid)
        print(json.loads(response.text))

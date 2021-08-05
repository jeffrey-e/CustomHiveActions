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
tags.append('misp')
query = In('tags', tags)
# print(str(query))
response = thapi.find_cases(query=query)
for returned_case in response.json():
    #if 'summary' in case:
    #    print(case['summary'])
    if returned_case['status'] == "Open":
        print("Found {} with id: {}".format(returned_case['title'].encode("utf-8"),returned_case['id']))
        case = Case()
        case.id = returned_case['id']
        case.summary = "<summary message>"
        case.status = "resolved"
        
        #Fields to update
        fields = ['status','summary']

        # Place actual request
        response = thapi.update_case(case,fields)
        #print json.loads(response.text)

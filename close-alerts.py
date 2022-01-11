import json
import getpass
from config import TheHive, Filters
from thehive4py.api import TheHiveApi
from thehive4py.query import In
import time

def __repr__(self):
    return str(self.__dict__)
hive_api_key = TheHive.get('key')
if not hive_api_key:
     hive_api_key = getpass.getpass(prompt='API Key: ', stream=None)

thapi = TheHiveApi(TheHive.get('url', None),
        hive_api_key,
        TheHive.get('password', None),
        TheHive.get('proxies'),
        TheHive.get('verify'))

tags = Filters.get('tags')
if tags:
    query = In('tags', tags)
else:
    print('Missing tags to query')
    exit()

# query = Eq('source', 'MISP-extern')
# alertNew = Eq('status', 'New')
# query = And(sourceMISP, alertNew)

# print(str(query))
response = thapi.find_alerts(query=query)
# print(json.loads(response.text))

response.raise_for_status()

for returned_alert in response.json():
    # print(json.dumps(returned_alert))
    print(f"{returned_alert['id']}, {returned_alert['title']}, {returned_alert['status']}, {returned_alert['tags']}")
    # if 'summary' in case:
    #     print(case['summary'])
    if returned_alert['status'] == "New":
        print("Alert has status New. Marking as read...")
        # Grab alertid
        alertid = returned_alert['id']
        # Place actual request
        response = thapi.mark_alert_as_read(alertid)
        response.raise_for_status()
        print(f"Mark as read request response: {response.status_code}")
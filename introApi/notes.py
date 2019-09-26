import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import json
import xmltodict as xd

import amdataApi as api

# auth in this format is used in the amdataApi.py
auth = {'url':'https://amdata.proj.kth.se', 'user':'<user>', 'passwd':'<passwd>'}


# testing: getting a id-number for a global template 

tlist1 = api.templateId('Materials', auth)

# testing "requests" in user only space

tmpUser = auth['url'] + '/rest/template-version-manager/user/'

tlist2 = json.loads(requests.get(tmpUser, auth=(auth['user'], auth['passwd'])).text)


# chek whats in the portal

durl = auth['url'] + '/rest/data/query/'

tid = tlist2[0]['current']

dat = {"query": "{}", "templates": "[{\"id\":\""+tid+"\"}]", "all": "true"}

datalist = json.loads(requests.get(durl, data=dat, auth=(auth['user'], auth['passwd'])).text)


# retrieve saved data

datalist[0].keys()

dx = datalist[0]['xml_content']

dd = xd.parse(dx)
dd['root'].keys()


# save data

tpurl = auth['url'] + '/rest/template/' + str(tid)
tmpX = json.loads(requests.get(tpurl, auth=(auth['user'], auth['passwd'])).text)

# check
tmpX['content']

xw = xd.parse(tmpX['content'])

wk = xw['xsd:schema']['xsd:complexType']['xsd:sequence']['xsd:element']


# looking at types

typUser = auth['url'] + '/composer/rest/type-version-manager/user/' 
tylist = json.loads(requests.get(typUser, auth=(auth['user'], auth['passwd'])).text)

typId = tylist[-1]['current']

typUser1 = auth['url'] + '/composer/rest/type/' + str(typId)

tyX = json.loads(requests.get(typUser1, auth=(auth['user'], auth['passwd'])).text)


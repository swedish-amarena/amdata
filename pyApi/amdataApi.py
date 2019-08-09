# Copyright 2019 Niclas Stenberg
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# -------------------------------------------- API
import json                               # Python standard library
import requests                           # NEEDs to be installed
import xmltodict as xd
import pandas as pd
from io import StringIO

def sendBinaryFile(filename, auth):
    '''
    upload a file and returns the unique id for that file.
    
    blobId = matDB.sendBinaryFile(filename, auth)
    '''
    bloburl = auth['url'] + '/rest/blob/'
    requests.post(bloburl, files={'blob': open(filename, 'rb')},
                  auth=(auth['user'], auth['passwd']))
    hblob = json.loads(requests.get(bloburl, auth=(auth['user'],
                                                   auth['passwd'])).text)
    return hblob[-1]['id']


def getBinaryFile(dataId, filename, auth):
    '''
    download the raw data file that is associated with the dataid
    the name of the file is filename
    
    matDB.getBinaryFile(dataid, filename, auth)
    '''
    dd = getData(dataId,  auth)
    turl = auth['url']  + '/rest/template/' + dd['template']
    trt = requests.get(turl, auth)
    tr1 = json.loads(trt.content)
    td  = xd.parse(tr1['content'])
    tpl = td['xsd:schema']['xsd:element']['@name'] 
    grood = xd.parse(dd['xml_content'])
    blobid = grood[tpl]['blobid'] 
    bloburl = auth['url'] + '/rest/blob/download/' + blobid
    resp = requests.get(bloburl, auth=(auth['user'], auth['passwd']))
    if '200' in str(resp):
        with open(filename, 'wb') as f:
            f.write(resp.content)
    return resp


def addTemplate(filename, auth):
    '''
    adds a template to MDCS as global

    matDB.addTemplate('template_filename.xsd', auth)
    '''
    name = filename[:filename.rfind('.')]
    f = open(filename, 'r')
    tmplStr = ''
    for line in f:
        l1 = line.strip().replace('\t', '')
        tmplStr += l1.replace('  ', '')
    f.close()

    template = {'title': name, 'filename': filename, 'content': tmplStr}

    tmpGlobal = auth['url'] + '/rest/template/global/'
    requests.post(tmpGlobal, template, auth=(auth['user'], auth['passwd']))


def templateId(tmplName, auth):
    '''
    extracts the active id for the template with name tmplName
    If several templates exist with that name, the id for the latest one is
    returned

    tId = matDB.templateId(tmplName, auth)
    '''
    tmpGlobal = auth['url'] + '/rest/template-version-manager/global/'
    tlist = json.loads(requests.get(tmpGlobal, auth=(auth['user'],
                                                     auth['passwd'])).text)
    tid = 'None'
    for i in tlist:
        if i['title'] == tmplName:
            tid = i['current']

    return tid


def listData(auth, posts, templ):
    '''
    Searches for all the values of the desired template posts defined in the list *keys* with an
    addition of the specific keys: *'id'* and *'title'* which are
    separated from the template. 
    Returns a list with dicts where the keys values are.

    utlist = amdataApi.listData(auth, keys, templ)
    '''
    durl = auth['url'] + '/rest/data/query/'
    tid = templateId(templ, auth)
    dat = {"query": "{}", "templates": "[{\"id\":\""+tid+"\"}]", "all": "true"}
    datalist = json.loads(requests.get(durl, data=dat,
                                       auth=(auth['user'],
                                             auth['passwd'])).text)
    utlist = []
    print(type(datalist), len(datalist))
    print(datalist[0].keys())
    for ite in datalist:
        grood = xd.parse(ite['xml_content'])
        for kk in grood.keys():
            gkey = kk
        gro = grood[gkey]
        utdict = {'title': ite['title'], 'id': ite['id']}
        for kkk in keys:
            utdict[kkk] = gro[kkk]
        utlist.append(utdict)
    return utlist


def getData(dataId, auth):
    '''
    returns the whole data post for that Id in xml-format

    dataXml = matDB.getData(dataId, auth)
    '''
    durl = auth['url'] + '/rest/data/{}/'.format(dataId)
    data = json.loads(requests.get(durl, auth=(auth['user'],
                                               auth['passwd'])).text)

    return data



def makeGlobal(dataId, auth):
    '''
    Assigns the current data to the Global workspace
    
    makeGlobal(dataId, auth)
    '''
    durl = auth['url'] + '/rest/workspace/'
    wdata = json.loads(requests.get(durl, auth=(auth['user'],
                                               auth['passwd'])).text)
    for item in wdata:
        if "Global" in item['title']:
            wId = item['id']
    try:
        wurl = auth['url'] + '/rest/data/' + str(dataId) + '/assign/' + str(wId)
        sdresp = requests.patch(wurl, auth=(auth['user'], auth['passwd']))
    except:
        print('wId not found')

def sendData(mdata, auth):
    '''
    sends a filled dict to MDCS based on the chosen template
       required:  mdata['template']
       the rest of mdata[*] are mapped towards the template posts

    returns the response for success check

    resp = matDB.sendData(mdata, auth)
    '''
    tId = templateId(mdata['template'], auth)
    tpurl = auth['url'] + '/rest/template/' + str(tId)
    tmpX = json.loads(requests.get(tpurl, auth=(auth['user'],
                                                auth['passwd'])).text)
    print(tmpX)
    #
    # makes the content string based on template.
    #
    xw = xd.parse(tmpX['content'])
    wk = xw['xsd:schema']['xsd:complexType']['xsd:sequence']['xsd:element']
    print(wk)
    contentString ='<{}  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'.format(mdata['template'])
    for item in wk:
        keyt = item['@name']
        pres = '<' + keyt + '>'
        print(keyt+'\n')
        posts = '</' + keyt + '>'
        innehall = ''
        if keyt in mdata.keys():
            innehall = mdata[keyt]
        contentString += pres + innehall + posts

    contentString += '</{}>'.format(mdata['template'])
    durl = auth['url'] + '/rest/data/'
    data = { 'title': mdata['title'],
             'template': str(tId),
             'xml_content': contentString}
    # 
    print(data['title'])
    print(data['template'])
    print(data['xml_content'][0:100])
    sdresp = requests.post(durl, data, auth=(auth['user'], auth['passwd']))
    print('Done')
    print(sdresp)
    return sdresp


def saveAndMakeGlobal(mdataFull, auth):
    '''
    makes all necessary actions to save all data to MDCS

    resp = matDB.saveToDb(filename, mdataFull, dataCsv, auth)
    '''
    sdresp = sendData(mdataFull, auth)
    dList = listData(auth)
    dId = dList[-1]['id']
    makeGlobal(dId, auth)
    return sdresp



% A short introduction to the API that is used by the MDCS
% N. Stenberg


# Introduction

The MDCS works as a storage point for all structured data and meta data
that is derrived from Swedish research on materials for Additive
manufacturing (AM).

The MDCS has two ways of interaction, the web interface and the Rest
API. A Rest API is basically a couple of dedicated web pages where information
can be exchanged as opposed to a "full" API where information exchange
is separated from the web server.


# API background

The API documentation is on the web site

https://amdata.proj.kth.se/docs/api

click on **Help** and chose API documentation.


## Benefits with using the API

- Direct access to data
- can use python!
- can use whatever code You like!!
- save all overhead in files
- can write post/get scripts directly into calculation flows


# API and python3

Focus is on python3. Please do not use python2, it is not sustainable
taday.

RestAPIs have a dedicated python module, **requests**. which needs to
be installed. Some other data handling modules are needed too.

## Prerequisites

- requests
- numpy
- json
- xmltodict
- pandas
- io

Use pip or repositories based on preference. Some packages are only
available via pip.

If you run windows I think pip is the only way to go.

for pip, based on platform, use either:

```
$ pip install requests numpy json xmltodict pandas io
$ pip3 install requests numpy json xmltodict pandas io
$ python3 -m pip install requests numpy json xmltodict pandas io
```

# The *requests* function

*requests* works according to the documentation. 

![The documentation of the rest API is a web page where one can try
some functions](bilder/swagger1.png)

a typical get request looks like:

```
requests.get(URL, data={dict}, auth=(tuple))
```
For *post*, *delete*, *patch* just replace *get*.
The output is in some binary json format. If the output is interesting
parse the output via the json interpreter:

```
output = json.loads(requests.get('url', data={dict},
         auth=(tuple)).text)
```

## URL

The URL controls what type of request it is. Every specific request
all are posted to unique urls. For a full list of what a specific user
can do see the API documentation on the MDCS help page.

To post a dataset the URL = '<base_url>/rest/data'


##  data

The data is specified by what type of request it is. 

For instance, for a complete list of all the available templates data
is not needed and is therefore omitted in the request.

On the other hand, if a template shall be added the *post* command
needs to have the template information. That information is included
in the data dict.

```
data = {'title': name, 'filename': filename, 'content': tmplStr}
```

## auth

The MDCS is based around users and their accounts. Every post has
information of the owner. Therefore every user must be
authenticated. When the API is used that needs to be done every time a
request is done. auth contain the user name and password as strings in
a tuple.

```
auth = ( 'user', 'passwd' )
```


# The first version of the amdataApi package

A compilation of functions is supplied on github. The function shall
be seen as guidance to the API usage. They may be modified according
to your own needs. But,

**Please!** share your improvements! Others might find
them useful too. 

## How to use

Put the pyApi folder in your PYTHON_PATH. __init__.py will make
certain that python finds it. 

import:
```
from pyApi import amdataApi
```

and you are ready to go.


## The functions in amdataApi

First, all functions needed a *auth* dict thast contain all
authentifications including the location of the server.

Each user has its own credentials

```
auth = { 'url': 'https://amdata.proj.kth.se',
         'user': 'username',
		 'passwd': 'password'
	   }
```

### sendBinaryFile

Uploads a file and returns the unique id for that file. Is very useful
if the template has a 'blobid' field where it can be referenced. 

usage:

    blobId = amdataApi.sendBinaryFile(filename, auth)

### getBinaryFile

Downloads the binary file that is associated with the *dataid* where
the field *blobid* exists.

The name of the file that is downloaded will have the name *filename*

usage:
    
    amdataApi.getBinaryFile(dataid, filename, auth)
 
### addTemplate

Adds a template to MDCS as global. i.e. available to all.
The template must have been correctly formatted prior to sending it
the MDCS. See template documentation.

usage:

    amdataApi.addTemplate('template_filename.xsd', auth)


### templateId

Extracts the active *id* for the template with name *tmplName*

If several templates exist with that name, the id for the latest one is
returned

usage:

    tId = amdataApi.templateId(tmplName, auth)
	

### listData

Searches for all the values of the desired template posts defined in the list *keys* with an
addition of the specific keys: *'id'* and *'title'* which are
separated from the template. 
Returns a list with dicts where the keys values are.

usage:

    utlist = amdataApi.listData(auth, keys, templ)
 

### getData

Returns the whole data post for one *id* in xml-format

usage:

    dataXml = amdataApi.getData(dataId, auth)
	

### makeGlobal

Assigns the *dataId* to the Global workspace
    
usage:

    amdataApi.makeGlobal(dataId, auth)

### sendData

Sends a filled dict(*mdata*) to the MDCS based on the chosen template
       
**required in mdata**:  mdata['template']  (the given name of the template)

bacause the rest of mdata[*] are mapped towards the template posts

Returns the response for success check. 200 is OK!, the rest is error codes.

usage:

    resp = amdataApi.sendData(mdata, auth)



### saveAndMakeGlobal

Sends the data to the MDCS with the sendData function and makes the
data accessible to all.

usage:

    resp = amdataApi.saveAndMakeGlobal(mdataFull, auth):


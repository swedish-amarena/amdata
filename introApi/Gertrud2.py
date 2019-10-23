contentString = '<root  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><MaterialName>Johanna</MaterialName><YoungsModulus>200000000</YoungsModulus><PoissinsRatio>.3</PoissinsRatio></root>'

data = { 'title': 'Gertrud2',
             'template': str('5db05610e914bb320e7ada24'),
             'xml_content': contentString}
             
durl = auth['url'] + '/rest/data/'   
         
sdresp = requests.post(durl, data=data, auth=(auth['user'], auth['passwd']))


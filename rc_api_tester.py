#!/usr/bin/env python
from urllib import request, parse
# data
data = parse.urlencode( {                                                                       
     'token': '<token config needs to go here>',                               
         'content': 'project',                                                  
             'format': 'json',                                                  
                 'returnFormat': 'json'                                         
                 }).encode()
url = 'https://www.hcvtargetrc.org/api/'

req =  request.Request(url, data=data)
response = request.urlopen(req)

print(response.read().decode('utf-8'))

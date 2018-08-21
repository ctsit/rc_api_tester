#!/usr/bin/env python

# Purpose: 

# Version: 0.0.1

# Author(s): See AUTHORS file in repo. All rights reserved.

import configparser
from urllib import request, parse

# commandline arguments need to go here
## TODO: ARG: log_file_name:  need arg for loggfile name, needs default 
## TODO: ARG: log_file_path: need arg for log file location, needs default
## TODO: ARG: verbose: need arg so output will goto stdout? or maybe that shoudl be
##               default
## TODO: ARG: help: needs to print help options
## TODO: ARG: version: needs to pront version

# parse config from config.ini

config = configparser.ConfigParser()
config.read('config.ini')
config.sections()
token = config['DEFAULT']['Token']







# Api testing code below
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

# logging and options to goto stdout need to go here.
print(response.read().decode('utf-8'))

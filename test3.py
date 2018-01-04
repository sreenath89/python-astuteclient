#!/usr/bin/python
# -*- coding: utf-8 -*-
# list meters - client initialized with get_client
#imports
from ceilometerclient import client
from os import environ as env
from ceilometerclient.common import utils

#getting the credentials
keystone = {}
keystone['os_username']=env['OS_USERNAME']
keystone['os_password']=env['OS_PASSWORD']
keystone['os_auth_url']=env['OS_AUTH_URL']
keystone['os_tenant_name']=env['OS_TENANT_NAME']

#creating an authenticated client
ceilometer_client = client.get_client(2,**keystone)

#now you should be able to use the API
meters = ceilometer_client.meters.list()
print meters


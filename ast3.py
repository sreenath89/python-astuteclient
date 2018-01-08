#!/usr/bin/python
# -*- coding: utf-8 -*-
# list meters - client initialized with get_client
#imports
from astuteclient import client
from os import environ as env
from astuteclient.common import utils

#getting the credentials
keystone = {}
keystone['os_username']=env['OS_USERNAME']
keystone['os_password']=env['OS_PASSWORD']
keystone['os_auth_url']=env['OS_AUTH_URL']
keystone['os_tenant_name']=env['OS_TENANT_NAME']

#creating an authenticated client
astute_client = client.get_client(1,**keystone)

print astute_client
bt = astute_client.billing_types.list()

print bt

#now you should be able to use the API
#meters = astute_client.meters.list()
#print meters


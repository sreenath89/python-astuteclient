#!/usr/bin/python
# -*- coding: utf-8 -*-
# list meters - client initialized with lambda’d auth_token
from ceilometerclient import client
from os import environ as env
import keystoneclient.v2_0.client as ksclient

#getting the credentials
keystone = {}
keystone['username']=env['OS_USERNAME']
keystone['password']=env['OS_PASSWORD']
keystone['auth_url']=env['OS_AUTH_URL']
keystone['tenant_name']=env['OS_TENANT_NAME']

#creating a keystone client
ceilometer_client = client._get_ksclient(**keystone)
token = ceilometer_client.auth_token

#creating an endpoint
ceilo_endpoint = client._get_endpoint(ceilometer_client, **keystone)

#creating a ceilometer client
ceilometer = client.Client('2',endpoint = ceilo_endpoint, token = token)

#tests
meters = ceilometer.meters.list()
print meters

#!/usr/bin/env python

import code
import readline
import rlcompleter
import os
import glanceclient
from keystoneclient.v2_0 import client as keystone_client

os_vars = {'OS_PASSWORD': None,
           'OS_AUTH_URL': None,
           'OS_USERNAME': None,
           'OS_TENANT_NAME': None}

for os_var in os_vars.keys():
    try:
        os_vars[os_var] = os.environ[os_var]
    except KeyError:
        os_vars[os_var] = raw_input('%s: ' % os_var)


kclient = keystone_client.Client(
    username=os_vars['OS_USERNAME'],
    password=os_vars['OS_PASSWORD'],
    tenant_name=os_vars['OS_TENANT_NAME'],
    auth_url=os_vars['OS_AUTH_URL']
)

endpoint = kclient.service_catalog.url_for(
    service_type='image',
    endpoint_type='publicURL')

token = kclient.auth_token

gclient = glanceclient.client.Client(endpoint=endpoint + '/v1', token=token)

print("""
###################################################
# Glance API access available through 'gclient.*' #
# example: gclient.images.findall()               #
###################################################
""")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact()

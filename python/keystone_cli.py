#!/usr/bin/env python

import code
import readline
import rlcompleter
import os
from keystoneclient.v2_0 import client as keystone_client
import openstack_variables

osvars = openstack_variables.get()

kclient = keystone_client.Client(
    username=osvars['OS_USERNAME'],
    password=osvars['OS_PASSWORD'],
    tenant_name=osvars['OS_TENANT_NAME'],
    auth_url=osvars['OS_AUTH_URL']
)

print("""
#####################################################
# Keystone API access available through 'kclient.*' #
# example: kclient.roles.findall()                  #
#####################################################
""")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact()

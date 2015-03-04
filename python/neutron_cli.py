#!/usr/bin/env python

import code
import readline
import rlcompleter
import os
from neutronclient.v2_0 import client
import openstack_variables

osvars = openstack_variables.get()

nclient = client.Client(
    username=osvars['OS_USERNAME'],
    password=osvars['OS_PASSWORD'],
    tenant_name=osvars['OS_TENANT_NAME'],
    auth_url=osvars['OS_AUTH_URL'],
)

print("""
#################################################
# Nova API access available through 'mclient.*' #
# example: nclient.list_subnets()               #
#################################################
""")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact()

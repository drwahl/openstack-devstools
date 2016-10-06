#!/usr/bin/env python

import code
import readline
import rlcompleter
import os
from novaclient.v2 import client
import openstack_variables

osvars = openstack_variables.get()

nclient = client.Client(
    osvars['OS_USERNAME'],
    osvars['OS_PASSWORD'],
    osvars['OS_TENANT_NAME'],
    osvars['OS_AUTH_URL'],
    no_cache=True
)

print("""
#################################################
# Nova API access available through 'nclient.*' #
# example: nclient.flavors.list()               #
#################################################
""")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact()

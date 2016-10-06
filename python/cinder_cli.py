#!/usr/bin/env python

import code
import readline
import rlcompleter
import os
from cinderclient.v1 import client
import openstack_variables

osvars = openstack_variables.get()

cclient = client.Client(
    osvars['OS_USERNAME'],
    osvars['OS_PASSWORD'],
    project_id=osvars['OS_TENANT_NAME'],
    auth_url=osvars['OS_AUTH_URL'],
)

print("""
#################################################
# Nova API access available through 'cclient.*' #
# example: cclient.volumes.list()               #
#################################################
""")

vars = globals()
vars.update(locals())
readline.set_completer(rlcompleter.Completer(vars).complete)
readline.parse_and_bind("tab: complete")
shell = code.InteractiveConsole(vars)
shell.interact()

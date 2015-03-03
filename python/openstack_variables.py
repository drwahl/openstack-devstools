#!/usr/bin/env python

import os


def get():
    os_vars = {'OS_PASSWORD': None,
               'OS_AUTH_URL': None,
               'OS_USERNAME': None,
               'OS_TENANT_ID': None,
               'OS_TENANT_NAME': None}

    for os_var in os_vars.keys():
        try:
            os_vars[os_var] = os.environ[os_var]
        except KeyError:
            os_vars[os_var] = raw_input('%s: ' % os_var)

    return os_vars

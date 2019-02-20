#!/usr/bin/env python3

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import sys, re

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:


        # Simple RPC
        selected  = client.call("ak.wwise.ui.getSelectedObjects")['objects']

        if len(selected) == 0:
            sys.exit('no object selected')

        pprint(selected)

        # RPC with options
        # return an array of all children objects in the default actor-mixer work-unit
        args = {
            "from": {"id": [selected[0]['id']]},
            "transform": [
                {"select": ['children']}
            ]
        }
        options = {
            "return": ['id', 'name','type']
        }
        children = client.call("ak.wwise.core.object.get", args, options=options)['return']
        pprint(children)

        for child in children:
            # match = re.search('(?P<note>.*)', name)
            print(child['name'])


except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

#!/usr/bin/env python3

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import sys, re
notes = ['c','c#','d', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

def note_name_to_number(name):
    note = 60
    match = re.search('(?P<letter>[cdefgabCDEFGAB]#?)(?P<octave>[0-9]+)', name)
    if match is not None:
        letter = match.group('letter').lower()
        octave = int(match.group('octave'))

        note = notes.index(letter)
        note = note + (octave + 2) * 12
        
    return note

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
            print(child['name'])
            match = re.search('(?P<note>[cdefgabCDEFGAB]#?[0-9]+)', child['name'])
            if match is not None:
                print(note_name_to_number(match.group('note')))
                


except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

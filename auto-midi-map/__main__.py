#!/usr/bin/env python3

from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import sys, re, math
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
            raise Exception('Please select an object')

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

        errors = []
        for child in children:
            name = child['name']

            match = re.search('(?P<note>[cdefgabCDEFGAB]#?[0-9]+)', name)
            if match is None:
                errors.append('Could not find a note in ' + name)
            else:
                child['note'] = note_name_to_number(match.group('note'))

        if len(errors) > 0:
            raise Exception('\n'.join(errors))
        
        # Try to fill whole between notes
        children.sort(key=lambda object: object['note'])
        
        i = 0
        for child in children:
            min = 0
            max = 127
            if i != 0:
                min = children[i - 1]['@MidiKeyFilterMax'] + 1
            if i != len(children) - 1:
                max = children[i]['note'] + math.floor((children[i + 1]['note'] - children[i]['note']) / 2)

            child['@MidiKeyFilterMin'] = min
            child['@MidiKeyFilterMax'] = max
            max = 127

            i += 1

        # pprint(children)
        for child in children:
            for key, value in child.items():
                if key.startswith('@'):
                    setProperty = {
                        'object': child['id'],
                        'property': key[1:],
                        'value': value
                    }
                    children = client.call("ak.wwise.core.object.setProperty", setProperty)


except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

except Exception as e:
    print(str(e))
    input("Press key to continue...")
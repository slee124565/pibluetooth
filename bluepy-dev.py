#!/usr/bin/env python

from bluepy.btle import *
import json

addr = ''
dev = Peripheral(addr,ifcae=0)
result = []
for s in dev.getServices():
    entry = {
        'uuid': s.uuid.binVal,
        'name': s.uuid.getCommonName()
        'characteristics':[]
        }
    for c in service.getCharacteristics():
        entry['characteristics'].append({
            'readable': c.supportsRead(),
            'uuid': c.uuid.binVal,
            'name': c.uuid.getCommonName()
            })
    result.append(entry)

print(json.dumps(result,indent=2))
print('\n')


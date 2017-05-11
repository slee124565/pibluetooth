#!/usr/bin/env python

from bluepy.btle import *
import json

addr = 'B4:99:4C:66:A1:51'
dev = Peripheral(addr,iface=0)
result = []
for s in dev.getServices():
    entry = {
        #'uuid': str(s.uuid.binVal),
        'name': s.uuid.getCommonName(),
        'characteristics':[]
        }
    for c in s.getCharacteristics():
        entry['characteristics'].append({
            'readable': c.supportsRead(),
            #'uuid': str(c.uuid.binVal),
            'name': c.uuid.getCommonName(),
            'pstring': c.propertiesToString()
            })
        #if c.supportsRead():
        #    entry['value'] = c.read()
    result.append(entry)

print(json.dumps(result,indent=2,encoding='utf-8'))
print('\n')
#print('%s\n' % str(result))


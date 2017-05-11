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
        data = {
            'readable': c.supportsRead(),
            #'uuid': str(c.uuid.binVal),
            'name': c.uuid.getCommonName(),
            'pstring': c.propertiesToString()
            }
        if c.supportsRead() and entry['name'] == 'Device Information':
            data['value'] = str(dev.readCharacteristic(c.getHandle()))
        entry['characteristics'].append(data)
    result.append(entry)

#print(json.dumps(result,indent=2))
#print('\n')
print('%s\n' % str(result))

with open('result.json','w') as fh:
    fh.write(str(result))



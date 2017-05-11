#!/usr/bin/env python

from bluepy.btle import *
import json
import sys

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
        if c.propertiesToString() == 'READ ':
            value = bytearray()
            value.extend(dev.readCharacteristic(c.getHandle())) 
            data['value_hex'] = ','.join('0x{:02x}'.format(x) for x in value)
        entry['characteristics'].append(data)
    result.append(entry)

print(json.dumps(result,indent=2))
print('\n')
#print('%s\n' % str(result))
#sys.exit(0)

with open('result.json','w') as fh:
    fh.write(json.dumps(result,indent=2))



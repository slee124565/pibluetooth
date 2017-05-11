#!/usr/bin/env python

from bluepy.btle import *
import sys

addr = 'B4:99:4C:66:A1:51'
dev = Peripheral(addr,iface=0)

for c in dev.getCharacteristics:
    if c.uuid.getCommonName() == 'ea52':
        data_hex = '06,13,80,00,01,94'
        val = bytearray([int(n,16) for n in data_hex.split(',')])
        dev.writeCharacteristic(c.getHandle(),val,withResponse=True)
        val = bytearray()
        val.extend(dev.readCharacteristic(c.getHandle()))
        val_hex = ','.join('0x{:02x}'.format(x) for x in val)
        sys.stderr.write('%s\n' % val_hex)
        break

 

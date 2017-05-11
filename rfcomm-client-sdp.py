#!/usr/bin/env python

import bluetooth

sampo = 'B4:99:4C:66:A1:51'
yalebox = 'B8:27:EB:6C:D7:6F'
s6 = '8C:BF:A6:47:DE:4A'
mi = '88:0F:10:2E:45:7D'
danalock = 'EC:FE:7E:14:0F:E6'
bdaddr = danalock

services = bluetooth.find_service(address=bdaddr)

print('find address %s services:\n' % bdaddr)
for service in services:
    for key in service:
        print('key: %s, value:%s\n' % (key,service[key]))
    print('====\n')



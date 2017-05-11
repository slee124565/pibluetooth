#!/usr/bin/env python

import bluetooth

bdaddr = ''

services = bluetooth.find_service(address=bdaddr)

for service in services:
    for key in service:
        print('key: %s, value:%s' % (key,service[key]))
    print('====')



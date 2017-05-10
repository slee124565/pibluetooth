i#!/usr/bin/env python


import bluetooth

bd_addr = "B8:27:EB:F5:4D:BD" # flh-mirror
bd_addr = "B8:27:EB:6C:D7:6F" # flh-yalebox

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()


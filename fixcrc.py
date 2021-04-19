import sys
import crcmod
import os

input_filenames = sys.argv[1:]
if not input_filenames:
    exit()

for filename in input_filenames:
    print("Fixing CRC at end of ", filename, "...")
    file = open(filename, "rb")
    data = file.read()
    file.close()
    content = data[:-2]
    crc = data[-2:]
    xmodem_crc_func = crcmod.predefined.mkCrcFun('xmodem')
    newcrc = xmodem_crc_func(content)
    print("Old CRC: ","".join(map(hex, crc)).replace("0x","").expandtabs(4))
    print("Computed CRC: ", hex(newcrc))
    
    newcrcbytes = newcrc.to_bytes(2,"big")
    file = open(filename, "wb")
    file.write(content)
    file.write(newcrcbytes)
    file.close()
    print("CRC fixed.")

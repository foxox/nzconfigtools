import os
import hashlib
import crcmod

filename = "G:\\NCSET006.BIN"
file = open(filename, "rb")

if not file:
    print("problem opening file to read")
    exit()

data = bytearray(file.read())
# print(len(data))
file.close()

# change file here:

def assign(menu, menu_idx, value):
    for index in menu:
        data[index+menu_idx*4] = value

def access(menu, menu_idx):
    return data[menu[0]+menu_idx*4]


maspa_offset = 169824
u1_offset = 183080
u2_offset = 189708
u3_offset = 196336
mode_id_suboffset = 1240
i_menu_suboffset = 924

# indexes in order of importance -- first one may be necessary, others clones with no effect on the z5
# maspa_imenu = [170748, 177376]
# u1_imenu = [184004]
# u2_imenu = [190632]
# u3_imenu = [197260]

# offset=0
# print(offset)
# for i in range(0,12):
#     assign(u1_imenu, i, i+offset)
#     assign(u2_imenu, i, i+offset+1)
#     assign(u3_imenu, i, i+offset+2)
#     # assign(maspa_imenu, i, access(u1_imenu, i))


mode_id_p = 29
mode_id_s = 30
mode_id_a = 31
mode_id_m = 32
mode_id_auto = 33

data[u1_offset+mode_id_suboffset] = mode_id_p
data[u2_offset+mode_id_suboffset] = mode_id_s
data[u3_offset+mode_id_suboffset] = mode_id_auto


file = open(filename, "wb")

if not file:
    print("problem opening file to write")
    exit()

file.write(bytes(data))

os.system("python fixcrc.py " + filename)






exit()




content0 = data0[:-2]
content1 = data1[:-2]

outfile0 = open("content0.bin", "wb")
outfile1 = open("content0.bin", "wb")
outfile0.write(content0)
outfile1.write(content1)
outfile0.close()
outfile1.close()

twobytemax = 65535

# print("hashlib")
# #ruled out: shake_128 shake_256
# hasher = hashlib.sha1()
# hasher.update(content0)
# digest = hasher.hexdigest()
# print(digest)
# #  % twobytemax)

# print("sum mod")
# print(hex(sum(content0)%twobytemax))

print("crcmod")
# poly = 256
# poly16=int('10000000000000000',2)
# poly16lower = poly16-1
# for reverse in [True, False]:
#   print("Reverse: ", reverse)
#   for i in range(0,poly16lower-60000):
#     poly = poly16+i
#     poly=int("1021",16)
#     if i%128==0:
#       sys.stdout.write("test {0}".format(round(100*i/poly16lower)) + "%\r")
#       sys.stdout.flush()
#     # print("poly: ", poly)
#     # print(hex(poly))
#     crc = crcmod.Crc(poly, rev=reverse)
#     #, initCrc=0, xorOut=0xFFFFFFFF)
#     # assert(crc.digest_size == 2)
#     crc.update(content0)
#     digest = crc.hexdigest()
#     if digest == int("3e71",16):
#       print("digest: ", digest)

# poly=int("11021",16)
# crc = crcmod.Crc(poly, rev=False, initCrc=0x31c3)
# crcmod.predefined.XMODEM
# crc.update(content0)
# digest = crc.hexdigest()
# print(digest)

xmodem_crc_func = crcmod.predefined.mkCrcFun('xmodem')
print(hex(xmodem_crc_func(content0)))


#width=16  poly=0x1021  init=0x0000  refin=false  refout=false  xorout=0x0000  check=0x31c3  residue=0x0000  name="CRC-16/XMODEM"

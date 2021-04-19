import os
import sys

argc = len(sys.argv)
if argc < 4:
    print("Provide a filename, a number indicating which user setting to change (1 for U1, etc.), and then provide the mode to change it to (auto for auto, m for manual, a for aperture priority, s for shutter priority, p for program).")
    exit()
filename = sys.argv[1]
print("Using file", filename)

user_mode_num = min(3, max(1, int(sys.argv[2]))) if argc > 2 else 1

mode_ids = {"P":29, "S":30, "A":31, "M":32, "AUTO":33}

desired_mode = sys.argv[3].upper()
if not desired_mode in mode_ids:
    print(f"Invalid mode \"{desired_mode}\" provided. Use AUTO, M, A, S, or P.")
    exit()

file = open(filename, "rb")
if not file:
    print("Error opening file to read config.")
    exit()

data = bytearray(file.read())
file.close()

maspa_offset = 169824
u_offsets = {1:183080, 2:189708, 3:196336}
mode_id_suboffset = 1240
i_menu_suboffset = 924

print(f"Changing U{user_mode_num} mode to {desired_mode}.")
data[u_offsets[user_mode_num]+mode_id_suboffset] = mode_ids[desired_mode]

file = open(filename, "wb")

if not file:
    print("Error opening file to write config changes back.")
    exit()

file.write(bytes(data))
file.close()

print("Done changing mode.")

os.system("python fixcrc.py " + filename)

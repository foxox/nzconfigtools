import os
import sys

argc = len(sys.argv)
if argc < 2:
    print("Provide a filename and optionally a number indicating which custom settings mode to move to the maspa settings, for example 1 for U1.")
    exit()
filename = sys.argv[1]
print("Using file", filename)

user_mode_num = min(3, max(1, int(sys.argv[2]))) if argc > 2 else 1
print("Using user mode number", user_mode_num)

file = open(filename, "rb")
if not file:
    print("Error opening file to read config.")
    exit()

data = bytearray(file.read())
file.close()

assert(1 <= user_mode_num <= 3)

# Length of a config section
sec_len = 6628
# Beginning of the M/A/S/P/Auto config section
maspa_start = 169824
# Beginning of the U1/U2/U3 config section
user_start = 183080 + (user_mode_num-1) * sec_len
user_settings = data[user_start:user_start+sec_len]

user_settings_copy = user_settings.copy()
user_settings_copy[924:972:4] = [3]*12
data[maspa_start:maspa_start+sec_len] = user_settings_copy
data[maspa_start+sec_len:maspa_start+2*sec_len] = user_settings_copy

# Move the settings from the selected user mode to MASPA
data[maspa_start:maspa_start+sec_len] = user_settings
# The following is a duplicated location for MASPA settings.
# This duplicate seems to be ignored when the file is loaded in the camera, so we can just leave it.
# data[maspa_start+sec_len:maspa_start+2*sec_len] = user_settings

print(f"Copied user settings from U{user_mode_num} to the M/A/S/P/Auto settings slots.")

file = open(filename, "wb")
if not file:
    print("Error opening file to write config changes back.")
    exit()

file.write(bytes(data))
file.close()

os.system("python fixcrc.py " + filename)

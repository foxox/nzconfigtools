import sys
from lib.diff import *

argc = len(sys.argv)
if argc < 3:
  print("Provide two filenames as inputs on the command line.")
  exit()

file0 = open(sys.argv[1], "rb")
file1 = open(sys.argv[2], "rb")

data0 = file0.read()
data1 = file1.read()

file0.close()
file1.close()

data = list(zip(data0, data1))

ranges = compute_diff_ranges(data)
print_diffs(data, ranges, 5)

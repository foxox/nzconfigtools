from lib.diff import *
import os
import shutil

# todo: https://docs.python-guide.org/writing/structure/

def test_lib_diff():
    print("test_lib_diff")
    data = list(zip([0,4,1,5,6,0], [2,4,2,5,7,7]))
    ranges = compute_diff_ranges(data)
    assert(ranges == [[0,0],[2,2], [4,5]])

def test_diff():
    print("test_diff")
    os.system("python diff.py tests/S0.BIN tests/S1.BIN")
    # todo: do more here than exercise it

def test_fixcrc():
    print("test_fixcrc")
    tmpfilename = "tests/generated_by_unit_test.BIN"
    shutil.copyfile("tests/S0.BIN", tmpfilename)
    os.system("python fixcrc.py " + tmpfilename)
    os.remove(tmpfilename)
    # todo: do more here than exercise it

def test_copyconfig():
    print("test_copyconfig")
    tmpfilename = "tests/generated_by_unit_test.BIN"
    shutil.copyfile("tests/S0.BIN", tmpfilename)
    os.system("python copyconfig.py " + tmpfilename) # default to 1
    os.system("python copyconfig.py " + tmpfilename + " 1")
    os.system("python copyconfig.py " + tmpfilename + " 2")
    os.system("python copyconfig.py " + tmpfilename + " 3")
    # handle bad usermode number
    os.system("python copyconfig.py " + tmpfilename + " 4")
    os.system("python copyconfig.py " + tmpfilename + " 0")
    os.remove(tmpfilename)
    # todo: do more here than exercise it

print("Testing...")
test_lib_diff()
test_diff()
test_fixcrc()
test_copyconfig()
"""
    Exception
"""

import sys

print(sys.platform)
def is_it_linux():
    assert('linux' in sys.platform), "fungsi ini hanya untuk linux"
is_it_linux()

name = "budi"

try:
    print(i + name)
except :  #except NameError:
    print("ada yg salah dari i + name")

raise Exception("stop ada yg salah")#menghentikan program

print(i+ objek)
import os
import sys

if sys.argv[1] == 'mac':
    os.system("python FindMacbook.py > tmp.txt")
elif sys.argv[1] == 'iphone':
    os.system("python FindIphone7s.py > tmp.txt")
else:
    print "mac or iphone?"
    exit(0)

os.system("python ContentFilter.py tmp.txt > output.txt")
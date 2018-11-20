#!usr/bin/python3
import subprocess
import sys
import re

var1 = sys.argv[1]
temp = 'ls -aFl ' + var1

ls = subprocess.Popen(temp,shell = True, stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

ls1 = []
directory = 0
file_num = 0
result = []
ls1 = ls.splitlines()
for i in ls1:
    
    if i.endswith('./'):
        directory = directory + 1

    elif i.startswith('d'):
        directory = directory + 1
        result.append(i)
    elif i.startswith('t'):
        print("")
    else:
        file_num = file_num + 1
        result.append(i)

result1 = ""

print("directory = %d, file %d" %(directory, file_num))
for item in result:
    item1 = re.split("\s+", item)
    print(item1[8],item1[4],item1[0])


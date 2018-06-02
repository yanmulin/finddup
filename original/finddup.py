#!/usr/bin/env python 

from checksum import create_checksum
from diskwalk import diskwalk

def finddup(path):
    d = diskwalk(path)
    paths = d.enumeratepaths()
    record = {}
    dup = []
    for p in paths:
        key = create_checksum(p)
        if key in record:
            dup.append(p)
        else :
            record[key] = p
    return dup

#if __name__ == "__ main__":
print("Hi")
dup = finddup("./test")
for path in dup:
    print(path)


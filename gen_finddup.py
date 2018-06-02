#!/usr/bin/env python

import os
import hashlib

def gen_enumeratepaths(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(dirpath, filename)

def gen_checksum(pathlist):
    for path in pathlist:
        md5obj = hashlib.md5()
        fp = open(path,"r")
        while True:
            data = fp.read(8196)
            if not data: 
                break
            md5obj.update(data)
        checksum = md5obj.digest()
        yield (checksum, path)

def gen_finddup(files):
    record = {}
    for item in files:
        if item[0] in record:
            yield item[1]
        else:
            record[item[0]] = item[1]
if __name__ == "__main__":
    pathlist = gen_enumeratepaths("./test")
    files = gen_checksum(pathlist)
    for dup in gen_finddup(files):
        print(dup)

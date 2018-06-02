#!/usr/bin/env python

import hashlib

def create_checksum(path):
    md5obj = hashlib.md5()
    fp = open(path,"r")
    while True:
        data = fp.read(8192)
        if not data:
            break
        md5obj.update(data)
    fp.close()
    return md5obj.digest()

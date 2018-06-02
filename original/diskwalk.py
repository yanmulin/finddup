#!/usr/bin/env python

import os

class diskwalk(object):
    def __init__(self, path):
        self.path = path;

    def enumeratepaths(self):
        path_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                fullpath = os.path.join(dirpath, f)
                path_collection.append(fullpath)
        return path_collection

    def enumeratefiles(self):
        file_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                file_collection.append(f)
        return file_collection

    def enumeratedirs(self):
        dir_collection=[]
        for dirpath, dirnames, filenames in os.walk(self.path):
            for d in dirnames:
                dir_collection.append(d)
        return dir_collection


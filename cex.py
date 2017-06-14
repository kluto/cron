# -*- coding: utf-8 -*-
from datetime import datetime
import os

def stamp_it():
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # fpath = os.path.join(os.path.expanduser('~'),'project/cron/cronlog.txt')
    froot = '/home/tpk/projects/cron/'
    fpath = froot + 'cronlog' + datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
    f = open(fpath, "a+")
    f.write("Script executed @ "+dt+"\n")
    f.close

if __name__ == '__main__':
    stamp_it()

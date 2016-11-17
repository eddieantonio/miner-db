#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Command line interface to the Miner database.
"""

import sqlite3
import argparse

from path import Path

from miner_db import Database


parser = argparse.ArgumentParser()
parser.add_argument('database', type=Path)
parser.add_argument('hash')
parser.add_argument('-s', '--show-source', action='store_true')

args = parser.parse_args()

path = 'file:' + args.database.abspath() + '?mode=ro'
conn = sqlite3.connect(path, uri=True)
db = Database(conn, read_only=True)

repo, file_info = db.get_info(args.hash)

print("{r.owner}/{r.name} license: {r.license}".format(r=repo))
print(file_info.path)

if args.show_source:
    print()
    print(file_info.source)

#!/usr/bin/env python3

import os
import pprint

fns = {}

with os.scandir() as it:
  for entry in it:
    if not entry.name.startswith('.') and entry.is_file():
      stat = entry.stat()
      print(entry.name[:4], entry.name, stat.st_mtime)
      try:
        fns[entry.name[:4]][entry.name] = stat.st_mtime
      except KeyError:
        fns[entry.name[:4]] = {entry.name: stat.st_mtime}
pprint.pprint(fns)
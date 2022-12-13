#!/usr/bin/env python3

import os
import pprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
  @staticmethod
  def on_created(event):
    if event.is_directory:
      return None

    if event.event_type == 'created':
      fn = event.src_path.split('/')[-1]
      print(f"New file created: {fn}")
      print(f'First 4 characters are: {fn[:4]}')

observer = Observer()
event_handler = Handler()
observer.schedule(event_handler, '.')
observer.start()
try:
  while observer.is_alive():
    observer.join(60) # Sit and wait for events
finally:
  observer.stop()
  observer.join()



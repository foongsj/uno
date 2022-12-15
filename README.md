# uno

This script uses watchdog to handle new file creation in a directory. On file creation, it moves all older files with the same 4 characters to the archive directory.

The user can change the Handler class to decide what to do when a directory change is detected.

The watchdog library uses Linux ionotify and handles the callback on the directory write. While waiting for callback, the script pauses and does not use any CPU resource.  Currently the script waits forever, but the user can choose to a timeout too (which doesn't really change anything as currently it loops).

#!/usr/bin/python

import os, time
#from django.conf import settings

# crontab -e in terminal
# 0 0 * * * /usr/bin/python $HOME/comparator/comparator/cron/file_deleter.py (save)

# monitor cron
# && curl -sm 30 k.wdt.io/<email>/<cron-name>?c=0_0_*_*_*


os.system("touch crons.txt")

# now = time.time ()
#
#
# def delete_file (path):
#     for file in os.listdir (path):
#         file = os.path.join (path, file)
#         file_old = is_file_old (file)
#         if os.path.isfile (file):
#             if file_old:
#                 os.remove (file)
#         elif os.path.isdir (file):
#             if file_old:
#                 os.rmdir (file)
#             else:
#                 delete_file (file)
#
#
# def is_file_old (file):
#     if os.stat (file).st_mtime < now - 18 * 86400:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     import_file_dir = settings.MEDIA_ROOT
#     output_file_dir = settings.OUTPUT_ROOT
#
#     # checking uploaded file dir for deletion
#     delete_file (import_file_dir)
#     # checking output file dir for deletion
#     delete_file (output_file_dir)

import os
import string
import shutil
import sys


def is_download_complete(item):  # Function to check if download is complete
    if item.endswith('!ut'):
        return False
    elif os.path.isdir(item):  # check if folders contain files still being torrented
        # os.chdir(item)
        for file in os.listdir(item):
            if file.endswith('!ut'):
                return False
        return True
    else:
        return True

import os
import string
import shutil
import sys

# def is_download_complete(main_dir, item):  # Function to check if download is complete
#     try:
#         if item.endswith('!ut'):
#             return False
#         elif os.path.isdir(item):  # check if folders contain files still being torrented
#             # os.chdir(item)
#             for item in os.listdir(item):
#                 current_path = os.path.join(main_dir, item)
#                 #next_path = os.path.join(current_path, item)
#                 return is_download_complete(current_path, item) 
#         else:
#             return True
#     except:
#         print(sys.exc_info, "Error occured when checking if {} download is complete".format(item))

def is_download_complete(main_dir, item):  # Function to check if download is complete
    
    current_path = os.path.join(main_dir, item)
    if item.lower().endswith('!ut'):
        return False

    elif os.path.isdir(current_path):  # check if folders contain files still being torrented
        # os.chdir(item)
        for file in os.listdir(current_path):
            #print(file)
            next_path = os.path.join(current_path, file)
            return is_download_complete(next_path, file) # employ recursivity for folders within folders
            # if file.lower().endswith('!ut'):
            #     return False
        return True
    else:
        return True


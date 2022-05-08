import os


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


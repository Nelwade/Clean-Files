import os


def is_download_complete(main_dir, item):  # Function to check if download is complete
    
    current_path = os.path.join(main_dir, item)
    if os.path.isfile(current_path):
        if "!ut" in item.lower():
            #print(item)
            return False
        

    elif os.path.isdir(current_path):  # check if folders contain files still being torrented
        # os.chdir(item)
        for file in os.listdir(current_path):
            #next_path = os.path.join(current_path, file)
            if is_download_complete(current_path, file) == False:
                return False
            # return is_download_complete(current_path, file)
    return True


# for item in os.listdir("E:/"):
#     try:
#         result = is_download_complete("E:/", item)
#         print("{}:   {}".format(item, result))
#     except PermissionError as error:
#         print("{}:   {}".format(item, error))
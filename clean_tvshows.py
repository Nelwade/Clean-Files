import os
import string
import shutil
import sys
import is_download_complete

def clean_tvshows(main_dir):

    # change into the directory to allow creation of directories and moving of files
    os.chdir(main_dir)
    
    #check if the folder named Series exists, if it does not create the folder
    if os.path.exists('Series'):
        current_path = os.path.join(main_dir, 'Series')
    else: 
        os.mkdir('Series')
        current_path = os.path.join(main_dir, 'Series')
        print("Creating Series Folder")
    
    
    # Iterate through the contents of the directory
    for item in os.listdir(main_dir):
        try:

            if item.endswith('mkv') or item.endswith('mp4') or 'S0' in item or 'Season' and 'Complete' in item:
                # Filter out videos and Tv shows in folders with "
                if is_download_complete.is_download_complete(item):              

                    folder_name = ""

                    if "." in item:
                        name = item.split(".")
                    else:
                        name = item.split()
                        name.remove("Season")

                    for word in name:
                        word_punc = word.translate(str.maketrans(
                            '', '', string.punctuation))  # remove punctuation marks
                        if word_punc.isalpha():
                            folder_name += word + " "  # parse to leave a short name of tv show
                        else:
                            break

                    os.chdir(current_path) #change into the series folder

                    if os.path.exists(folder_name):
                        
                        # if a folder for the tv show already exists, copy into folder
                        sourcepath = os.path.join(main_dir, item.strip())
                        destpath = os.path.join(current_path, folder_name.strip())
                        
                        os.chdir(destpath) #change into tv show folder

                        if os.path.exists(item): # check if file already exists in tv show folder
                            print("{} already exists in folder, Deleting".format(item)) 
                            os.remove(sourcepath) #delete item
                        else:
                            shutil.move(sourcepath, destpath)
                            print("\nFolder exists, copying {} to {} folder".
                                    format(item, folder_name))
                    else:
                        print('\nCreating Folder named {}...'.format(folder_name))
                        # if folder does not exist, create folder
                        os.mkdir(folder_name)
                        # and copy into folder
                        print('\nNow copying {} to {} folder\n'.format(
                            item, folder_name))

                        sourcepath = os.path.join(main_dir, item.strip())
                        destpath = os.path.join(current_path, folder_name.strip())
                        shutil.move(sourcepath, destpath)
                else:
                    print('\nDownload of show {} is not complete\n'.format(item))
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))
from glob import glob
from win10toast import ToastNotifier
from clean_tvshows import notification_error

import os
import string
import shutil
import sys
import is_download_complete

notification = ToastNotifier() # creates a window notification

def clean_movies(main_dir):
    print("\n\n\nCleaning Movie Files......")
    notification.show_toast("Clean Files", "Cleaning Movie Files", duration = 30)
    # change into the directory to allow creation of directories and moving of files
    os.chdir(main_dir)

    if os.path.exists("Movies"):
        current_path = os.path.join(main_dir, "Movies")
    else:
        # if folder does not exist, create folder
        os.mkdir("Movies")
        current_path = os.path.join(main_dir, 'Movies')
        print('\nDid not find Movies Folder, Creating Movies Folder...')
    
    # returns a list of  files and folders in the directory that might be movies
    movie_list =glob('*[0-9]*')

    # Iterate through the contents of the directory
    for item in movie_list:
        try:
            if '1080p' in item or '720p' in item:
                # Filter out movies from tv shows "

                if "S0" not in item: 
                    if is_download_complete.is_download_complete(main_dir, item):

                        
                        #os.chdir(destpath)
                        os.chdir(current_path)

                        sourcepath = os.path.join(main_dir, item.strip())

                        if os.path.exists(item): # check if movie already exists in the movies folder
                            print("{} already exists in folder, Deleting".format(item))
                            
                            if os.path.isdir(item):
                                shutil.rmtree(os.path.join(sourcepath)) # delete if directory
                            else: 
                                os.remove(sourcepath) #delete if file
                        else:
                            shutil.move(sourcepath, current_path)
                            print('\nNow copying {} to Movies folder\n'.format(item))
                        
                    else:
                        print('\nDownload of movie {} is not complete\n'.format(item))
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))
            notification_error()
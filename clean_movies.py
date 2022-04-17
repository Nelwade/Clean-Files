import os
import string
import shutil
import sys
import is_download_complete

def clean_movies(main_dir):
    print("Cleaning Movie Files......")
    # change into the directory to allow creation of directories and moving of files
    os.chdir(main_dir)
    
    # Iterate through the contents of the directory
    for item in os.listdir(main_dir):
        try:

            if '1080p' in item or '720p' in item:
                # Filter out movies from tv shows "

                if "S0" not in item: 
                    if is_download_complete.is_download_complete(main_dir, item):

                        if os.path.exists("Movies"):
                            # if a Movies already exists, copy into folder
                            sourcepath = os.path.join(main_dir, item.strip())
                            destpath = os.path.join(main_dir, "Movies")
                            #shutil.move(sourcepath, destpath)
                            print("\nFolder exists, copying {} to Movies folder".
                                format(item))
                            
                            os.chdir(destpath)

                            if os.path.exists(item): # check if movie already exists in the movies folder
                                print("{} already exists in folder, Deleting".format(item))
                                
                                if os.path.isdir(item):
                                    shutil.rmtree(os.path.join(sourcepath)) # delete if directory
                                else: 
                                    os.remove(sourcepath) #delete if file
                            else:
                                shutil.move(sourcepath, destpath)
                        else:
                            print('\nDid not find Movies Folder, Creating Movies Folder...')
                            # if folder does not exist, create folder
                            os.mkdir("Movies")
                            # and copy into folder
                            print('\nNow copying {} to Movies folder\n'.format(
                                item))
                            sourcepath = os.path.join(main_dir, item.strip())
                            destpath = os.path.join(main_dir, 'Movies')
                            shutil.move(sourcepath, destpath)
                            
                    else:
                        print('\nDownload of movie {} is not complete\n'.format(item))
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))
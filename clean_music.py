import os
import string
import shutil
import sys
import is_download_complete

def clean_music(main_dir):

    # change into the directory to allow creation of directories and moving of files
    
    def check_if_music(main_dir, item): #function to check if file is a music file
        try:
            current_path = os.path.join(main_dir, item)
            if item.lower().endswith('mp3') or item.lower().endswith('flac') or 'FLAC' in item or 'Mp3' in item or 'Discography' in item or 'discography' in item or '320kbps' in item or 'Greatest Hits' in item:
                return True
            elif item == "Music":
                return False
            elif os.path.isdir(current_path): # incase of a directory
                for item in os.listdir(current_path):
                    next_path =os.path.join(current_path, item)
                    return check_if_music(next_path, item)      
            else:
                return False
        except:
            print(item, sys.exc_info)

    os.chdir(main_dir)
    
    #check if the folder named Series exists, if it does not create the folder
    if os.path.exists('Music'):
        current_path = os.path.join(main_dir, 'Music')
    else: 
        os.mkdir('Music')
        current_path = os.path.join(main_dir, 'Music')
        print("Creating Music Folder")
    
    
    # Iterate through the contents of the directory
    for item in os.listdir(main_dir):
        try:
            # check if file is a music file or folder
            if check_if_music(main_dir, item):    
                # check if the download is complete
                if is_download_complete.is_download_complete(item):
                
                    os.chdir(current_path)
                    
                    #where the file is being copied from
                    sourcepath = os.path.join(main_dir, item.strip())

                    if os.path.exists(item):
                        # if file/folder exists in the Music Folder
                        print("{} already exists in folder, Deleting".format(item)) 
                        os.remove(sourcepath) #delete item
                    else:
                        shutil.move(sourcepath, current_path)
                        print("\nNow copying {} to Music folder".
                                    format(item))
                else:
                    print('\nDownload of {} is not complete\n'.format(item))
                   
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))

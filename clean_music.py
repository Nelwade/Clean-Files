from glob import glob
from win10toast import ToastNotifier
from clean_tvshows import notification_error

import os
import string
import shutil
import sys
import is_download_complete

notification = ToastNotifier() # creates a window notification

def clean_music(main_dir):
    
    print("\n\n\nCleaning Music Files......")
    notification.show_toast("\n\n\nClean Files", "Cleaning Music Files", duration = 3)

    # def check_if_music(main_dir, item): #function to check if file is a music file
    #     try:
    #         current_path = os.path.join(main_dir, item)
    #         if item.lower().endswith('mp3') or item.lower().endswith('flac') or 'FLAC' in item or 'Mp3' in item or 'Discography' in item or 'discography' in item or '320kbps' in item or 'Greatest Hits' in item:
    #             return True
    #         elif item == "Music" or item == "Series" or item == "Movies":
    #             return False
    #         elif os.path.isdir(current_path): # incase of a directory
    #             for file in os.listdir(current_path):
    #                 next_path = os.path.join(main_dir, file)
    #                 return check_if_music(next_path, file)    #recursivity for folders within folders  
    #         else:
    #             return False
    #     except:
    #         print(sys.exc_info, "Error occurred in check_if_music for {}".format(item))
    
    
    # change into the directory to allow creation of directories and moving of files
    os.chdir(main_dir)
    
    #check if the folder named Series exists, if it does not create the folder
    if os.path.exists('Music'):
        current_path = os.path.join(main_dir, 'Music')
    else:
        os.mkdir('Music')
        current_path = os.path.join(main_dir, 'Music')
        print("\nDid not find Music Folder, Creating Music Folder")
    # Returns a set of al music files and folders in the directory
    music_list = set( glob('*mp3*') + glob('*kbps*') + glob('*discography*')+ glob('*flac*') + glob('*greatest hits*'))
    
    # Iterate through the contents of the directory
    for item in music_list:
        try:   
            # check if the download is complete
            if is_download_complete.is_download_complete(main_dir, item):
            
                os.chdir(current_path)
                
                #where the file is being copied from
                sourcepath = os.path.join(main_dir, item.strip())

                # if file/folder exists in the Music Folder
                if os.path.exists(item):
                    print("{} already exists in folder, Deleting".format(item))
                    if os.path.isdir(item):
                        shutil.rmtree(os.path.join(sourcepath)) # delete if directory
                    
                    else: 
                        os.remove(sourcepath) #delete if file
                else:
                    shutil.move(sourcepath, current_path)
                    print("\nNow copying {} to Music folder".
                                format(item))
            else:
                print('\nDownload of {} is not complete\n'.format(item))                   
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))
            notification_error()

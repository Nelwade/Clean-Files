# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Fri Apr  8 21:04:14 2022

@author: Owade
"""
import re
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


# main_dir name of the directory where you download your tv shows into, per episode
# it can take a user input


def sort_tvshows(main_dir):

    # change into the directory to allow creation of directories and moving of files
    # os.chdir(main_dir)
    # print(os.getcwd())

    # Iterate through the contents of the directory
    for item in os.listdir(main_dir):
        try:

            # print(item)

            # if item.endswith('!ut'):
            #    print('{} is incomplete'.format(item))
            #   continue

            if item.endswith('mkv') or item.endswith('mp4') or 'S0' in item or 'Season' and 'Complete' in item:
                # Filter out videos and Tv shows in folders with "
                # print(item)
                if is_download_complete(item):

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

                    if os.path.exists(folder_name):
                        # if a folder for the tv show already exists, copy into folder
                        sourcepath = os.path.join(main_dir, item.strip())
                        destpath = os.path.join(main_dir, folder_name.strip())
                        if os.path.exists(item):
                            print("{} already exists in folder".format(item)) #delete item
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
                        destpath = os.path.join(main_dir, folder_name.strip())
                        shutil.move(sourcepath, destpath)
                else:
                    print('\nDownload of {} is not complete\n'.format(item))
        except:
            print("{} did not move because of {}".format(
                item, sys.exc_info()))


def sort_movies(main_dir):
    # change into the directory to allow creation of directories and moving of files
    # os.chdir(main_dir)
    # print(os.getcwd())
    sort_tvshows(main_dir)  # put all tv shows into their folders first
    # Iterate through the contents of the directory
    for item in os.listdir(main_dir):
        try:

            if '1080p' in item or '720p' in item:
                # Filter out movies from tv shows "
                # print(item)
                if is_download_complete(item):

                    if os.path.exists("Movies"):
                        # if a Movies already exists, copy into folder
                        sourcepath = os.path.join(main_dir, item.strip())
                        destpath = os.path.join(main_dir, "Movies".strip())
                        shutil.move(sourcepath, destpath)
                        print("\nFolder exists, copying {} to Movies folder".
                              format(item))
                    else:
                        print('\nCreating Movies Folder...')
                        # if folder does not exist, create folder
                        os.mkdir("Movies")
                        # and copy into folder
                        print('\nNow copying {} to Movies folder\n'.format(
                            item))

                        sourcepath = os.path.join(main_dir, item.strip())
                        destpath = os.path.join(main_dir, 'Movies')
                        if os.path.exists(item):
                            print("{} already exists in folder".format(item)) #delete item
                        else:
                            shutil.move(sourcepath, destpath)
                else:
                    print('\nDownload of {} is not complete\n'.format(item))
        except:
            print("{} did not move".format(item))
            continue


# clean_folder("D:/Test_folder")
sort_movies('D:/')

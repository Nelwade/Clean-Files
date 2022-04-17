#!/usr/bin/env python3
"""
Created on Fri Apr  8 21:04:14 2022

@author: Owade
"""
import os
import sys
import clean_tvshows
import clean_movies
import clean_music
import datetime

# main_dir name of the directory where you download your tv shows into, per episode
# it can take a user input


def clean_disk(main_dir):
    
    time = datetime.datetime.now()
    print("\n\n", time, "\n-----------------------------------\n")

    clean_tvshows.clean_tvshows(main_dir) 
    clean_movies.clean_movies(main_dir) 
    clean_music.clean_music(main_dir)
    
# clean_disk("D:/")


# Manually creating logs to track all actions the program takes
# The path will vary according to where you want to store your logs
if os.path.exists(r'C:\Users\Stewie\Dropbox\My PC (DESKTOP-57VNQ1O)\Documents\Python projects\Clean Files\logs.txt'):
        with open('logs.txt', 'a') as logs:
            sys.stdout = logs
            clean_disk("D:/")
    
else:
    os.chdir(r'C:\Users\Stewie\Dropbox\My PC (DESKTOP-57VNQ1O)\Documents\Python projects\Clean Files')
    with open('logs.txt', 'w') as logs:
        sys.stdout = logs
        clean_disk("D:/")
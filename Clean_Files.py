#!/usr/bin/env python3
"""
Created on Fri Apr  8 21:04:14 2022

@author: Owade
"""
import os
import string
import shutil
import sys
import clean_tvshows, clean_movies, clean_music
import datetime


def clean_disk(main_dir):
    time = datetime.datetime.now()
    print("\n\n", time, "\n-----------------------------------\n")
    clean_tvshows.clean_tvshows(main_dir) 
    clean_movies.clean_movies(main_dir) 
    clean_music.clean_music(main_dir)
    # Manually creating logs to track all actions the program takes
    # The path woll vary according to where you want to store your logs
    
    
            
        
    

# main_dir name of the directory where you download your tv shows into, per episode
# it can take a user input



if os.path.exists(r'C:\Users\Stewie\Dropbox\My PC (DESKTOP-57VNQ1O)\Documents\Python projects\Clean Files\logs.txt'):
        with open('logs.txt', 'a') as logs:
            sys.stdout = logs
            clean_disk("D:/Test_folder")
    
else:
    os.chdir(r'C:\Users\Stewie\Dropbox\My PC (DESKTOP-57VNQ1O)\Documents\Python projects\Clean Files')
    with open('logs.txt', 'w') as logs:
        sys.stdout = logs
        clean_disk("D:/Test_folder")
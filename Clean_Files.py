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


def clean_disk(main_dir):
    clean_tvshows.clean_tvshows(main_dir)
    clean_movies.clean_movies(main_dir)
    clean_music.clean_music(main_dir)

# main_dir name of the directory where you download your tv shows into, per episode
# it can take a user input
clean_disk("D:/Test_folder")


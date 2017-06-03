# -*- coding: utf-8 -*-
"""
Created using Spyder

@author: aditya
"""
import os

def rename_files():
    
    #get current working directory
    saved_path=os.getcwd()
    
    #path for files
    new_path=r"C:\Users\aditya\version-control\udacity_ud036\prank"
    
    #get file names in a folder
    file_list = os.listdir(new_path)
    print file_list
    
    #change directory to find files
    os.chdir(new_path)
    
    #rename files
    for file_name in file_list:
        print file_name
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print file_name
        
    #change directory to saved path
    os.chdir(saved_path)
rename_files()
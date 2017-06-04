# -*- coding: utf-8 -*-
"""
Created on Spyder

@author: aditya
"""

import urllib

def read_text():
    file1 = open(r"C:\Users\aditya\version-control\udacity_ud036\movie_quotes.txt")
    contents = file1.read()
    print contents
    file1.close()
    check(contents)

def check(text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    print output
    connection.close()
    if "true" in output:
        print "Profanity alert"
    elif "false" in output:
        print "Text clean"
    else:
        print "Connection Error"

read_text()
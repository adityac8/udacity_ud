# -*- coding: utf-8 -*-
"""
Created using Spyder
Loop count 3
Waits for 10 seconds
Plays Maroon 5 Sugar
"""

import webbrowser
import time

total_breaks = 3
break_count = 0
print "This program started on "+time.ctime()
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=09R8_2nJtjg")
    break_count += 1

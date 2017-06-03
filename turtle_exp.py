# -*- coding: utf-8 -*-
"""
Created using Spyder
Exp file
All new code tried here

@author: aditya
"""

import turtle

#initialise turtle
brad=turtle.Turtle()

#see original position
original_pos = brad.pos()
print original_pos

#turtle cannot draw
brad.penup()

#set new position
brad.setpos(60,30)
new_pos = brad.pos()
print new_pos

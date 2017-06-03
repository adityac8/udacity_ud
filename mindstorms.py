# -*- coding: utf-8 -*-
"""
Created on Sat Jun 03 17:34:50 2017

@author: aditya
"""

import turtle

def draw_shape():
    
    #initialise screen
    window = turtle.Screen()
    
    #set screen color
    window.bgcolor("green")
    
    #initialise turtle
    brad = turtle.Turtle()
    
    #customising turtle
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    
    #make a square using turtle1
    no_of_squares = 36
    i = 0
    while i < no_of_squares:
        brad.right(10)
        sides = 4
        counter =0
        while counter < sides:
            brad.forward(100)
            brad.right(90)
            counter += 1
        i += 1
        
    #close window on click
    window.exitonclick()
    
draw_shape()
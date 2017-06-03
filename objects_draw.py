# -*- coding: utf-8 -*-
"""
Created using Spyder

Turtle Brad draws square
Turtle John draws circle
Turtle Flin draws triangle

@author: aditya
"""

import turtle

def draw_shape():
    
    #initialise screen
    window = turtle.Screen()
    
    #set screen color
    window.bgcolor("green")
    
    #initialise turtles
    brad = turtle.Turtle()
    john = turtle.Turtle()
    flin = turtle.Turtle()
    
    #customising turtle1
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    
    #customising turtle2
    john.shape("arrow")
    john.color("orange")
    john.speed(4)

    #customising turtle3
    john.shape("turtle")
    john.color("pink")
    john.speed(6)
    
    #make a square using turtle1
    sides = 4
    counter =0
    while counter < sides:
        brad.forward(100)
        brad.right(90)
        counter += 1
        
    #make a circle using turtle2 of radius 100
    john.circle(100)

    #make a triangle using turtle3
    sides = 3
    counter =0
    while counter < sides:
        flin.backward(100)
        flin.left(120)
        counter += 1

        
    #close window on click
    window.exitonclick()
    
draw_shape()
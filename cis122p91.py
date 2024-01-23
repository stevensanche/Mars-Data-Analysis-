'''
Title: CIS 122 Spring 2022 Project 9-1
Author: Steven Sanchez-Jimenez
Credits: CIS 122 Resources, Office Hours
Project: 9-1 Mars Data Analysis
'''
from turtle import *
import statistics
import random

def jump(x, y):
    '''
    move turtle without leaving a track to position (x,y).
    like turtle setpos but pen is always up for the move
    and put down after

    called from: display

    >>> jump(0,0)
    [return turtle to center]
    '''
    pu()
    setpos(x,y)
    pd()

    return

def rover_loc():
    '''
    return random number for rover location

    called from: collect_data

    >>> rover_loc()
    125 [for example]
    '''
    return random.randint(-275, 275)

def water_content():
    '''
    return random measure of water content on mars

    called from: collect_data

    >>> water_content()
    200 [for example]
    '''
    return random.randint(1, 290)

def temperature():
    '''
    return random measure of temperature on mars

    called from: collect_data

    >>> temperature()
    0 [for example]
    '''
    return random.randint(-178, 1)

# (optional)
def display(wc, t, x, y):
    '''
    display values of wc and t at pos x,y

    called from: main_explore_setup
    calls: jump
    '''
    jump(x-25, y+20)
    write(wc, font=('Arial', 12, 'normal'))
    jump(x, y+20)
    write(t, font=('Arial', 12, 'normal'))
    # return turtle to original position
    jump(x, y)

    return

def collect_data():
    '''
    remote control exploration of Mars:
        get new position (call rover_loc)
        send rover to the new position
        collect data there (call water_content and temp)
        display data there (optional display call)

    called from: mars_explore
    calls: rover_loc, water_content, temperature

    >>> collect_data()
    '''
    # get next position (x, y) for rover's explore path
    next_x = rover_loc()   
    next_y = rover_loc()   

    # send the rover there
    seth(towards(next_x, next_y))   # point rover
    stamp()                         # to show direction
    
    setpos(next_x,next_y)           # move the rover

    # gather data at this location
    wc = water_content()        
    t = temperature()

    # display the data
    print(next_x,'\t', next_y, '\t', wc, '\t', t)

    # challenge - display on the canvas
    display(wc, t, next_x, next_y)

    return (wc, t)

def mars_explore(stops):
    '''
    Repeatedly call mars_collect_data to gather
    data about temperature and water content on Mars.

    called from: mars_explore_main
    calls: collect_data

    >>> mars_explore(2)
    
    '''
    water = []
    temp = []
    for i in range(stops):
        collect_data()

    return 

def mars_explore_setup():
    '''
    set up printed and graphical output

    called from: mars_explore_main

    >>> mars_explore_setup()
    '''
    # print title line for printed output
    print('xpos', '\t',         # label for print output
          'ypos', '\t',         # note special char \t
          'water', '\t',        # which acts like the 
          'temp')               # tab key        

    # set up graphical output
    reset()
    title('Mars Rover')
    speed('fastest')
    display_color = 'blue'
    pencolor(display_color)
    dot(10, display_color)   # mark the rover's starting position

    return

def mars_explore_main():
    '''main function for mars_explore'''
    
    # set up printed and graphical environment
    mars_explore_setup()
    
    # explore Mars
    mars_explore(20)

    return

def analyze_data(li):
    '''
    This will calculate this mean, mode, and range
    
    >>> analyze_data([100, 100, 200])
    (133.33, [100], (100, 200))
    >>> analyze_data([-150, 0])
    (-75, [], (-150, 0))
    '''
    mean = round (statistics.mean(li), 2)    
    multi = statistics.multimode (li)
    range1 = min(li), max(li)
    if multi == li:
        multi = []
    return mean, multi, range1

print (analyze_data([-150, 0]))

def mars_report(dtype, dmean, dmode, drange):
    '''
    This will print out the result of data analysis
    
    Water Content Data Analysis
    range: 18 to 290
    mean: 131.35
    mode: [93]
    '''
    dtype =     

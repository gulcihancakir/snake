import time
import curses
import random
import os


score=0
y,x=15,1
snake ="x"
screen = curses.initscr() 
curses.curs_set(0)   
screen=curses.newwin(30,60,5,10)
screen.nodelay(1)

def main():
    screen.border(0)
    screen.addstr(0, 2, " Score:" + str(score))            
    screen.addstr(0, 20, " SNAKE GAME " )
    screen.addstr(0, 2, "Score: ")  


 
def moveright():
        global y,x
        x+=1
        
def moveleft():
        global y,x
        x-=1

def movedown():
        global y,x
        y+=1
        
def moveup():
        global y,x
        y-=1

direction =ord("D")

def move():
    global snake
    global direction
        
    screen.clear()
        
    key = screen.getch()
    direction = direction if key == -1 else key
    if(direction==ord("W")): moveup()      
    elif(direction==ord("D")): moveright()
    elif(direction==ord("S")): movedown()
    elif(direction==ord("A")): moveleft()
    screen.addstr(y,x,snake)
        
    main()
        
        

    screen.refresh()
    time.sleep(0.5)
        
                
while True:
        move()

        
curses.endwin()

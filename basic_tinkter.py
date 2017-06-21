'''
animation paper tutorial on page 164 python for kids
using tkinter
'''


def hello():
    print('hello there')


from tkinter import *
tk = Tk() # this creates an object of the class Tkinter and stores it in
# the variable called tk
# the Tk onject creates a window
# below we create a button and pass the tk variable as first parameter
btn = Button(tk,text= 'click me', command = hello)
btn.pack() # this tells the button to appear and arranges everything on the
# screen if there are other buttons


'''
NEXT
Creating a canvas for drawing
'''


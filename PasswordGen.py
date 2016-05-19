from Tkinter import *
import random
import argparse

PARSER = argparse.ArgumentParser(description='Password Generator')
TEST_ON = False

PARSER.add_argument('-a', '--autorun', default=False, nargs='?')

class PasswordGen (object):
    chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j'\
            ,'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D'\
            ,'E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y'\
            ,'Z','!','@','#','$','%','^','&','*','(',')','[',']','{','}','-','_','+','=',','\
            ,'.','?'] # Create Character List
            
    def callback(self): # Create function for button press
        random.shuffle(self.chars) # Shuffle character list
        self.pswd.set(''.join(self.chars[:self.maxlength+1])) # Set StringVar obj to pseudo-random password
    
    def __init__(self, lngnt): # Initialize class
        self.tk = Tk() # Create window
        self.maxlength = lngnt # set property 'maxlegnth' to the value of argumet 'lngnt'
        self.pswd = StringVar() # create StringVar to contain password 
        self.l = Label(self.tk,textvar=self.pswd) # create the view to show the password
        self.b = Button(self.tk, text="Generate!", command=self.callback) # create the button to generate password, calls method 'callback'
        self.l.pack() # Add widget 'self.l' to window 'self.tk'
        self.b.pack() # Add button widget 'self.b' to window 'self.tk'
        self.tk.bind_all('<Control-q>', self.destroy) # Bind the event for CTRL-Q with method 'destroy'
        self.tk.mainloop() # start mainloop to update window and keep window open

    def destroy(self, evt): # create event callback for quitting
        self.tk.destroy() # destroy window




if TEST_ON:
    t = PasswordGenerator

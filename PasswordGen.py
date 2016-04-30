from Tkinter import *
import random

class PasswordGen (object):
    chars = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j'\
            ,'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D'\
            ,'E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y'\
            ,'Z','!','@','#','$','%','^','&','*','(',')','[',']','{','}','-','_','+','=',','\
            ,'.','?']
    def callback(self):
        random.shuffle(self.chars)
        self.pswd.set(''.join(self.chars[:self.maxlength+1]))
    
    def __init__(self, lnght):
        self.tk = Tk()
        self.maxlength = lnght
        self.pswd = StringVar()
        self.l = Label(self.tk,textvar=self.pswd)
        self.b = Button(self.tk, text="Generate!", command=self.callback)
        self.l.pack()
        self.b.pack()
        self.tk.bind_all('<Control-q>', self.destroy)

    def destroy(self, evt):
        self.tk.destroy()




t = PasswordGen(10)
t.tk.mainloop()

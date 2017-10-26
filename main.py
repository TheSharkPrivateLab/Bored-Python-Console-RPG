# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:40:34 2017

@author: ccameron
"""
import tkinter as tk
from player import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, text="Hello World\n(clickme)", command=self.say_hi)
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Hi there, everyone!")

def initPlayer():
    
    p.assignEnemy(Enemy("Slime", 1, 5, 10));
    choice = input("Que faire ?\n");
    while choice != "exit":
        funcdict = {
          "attack": p.attack,
          "profile": p.showProfile,
          "exit": exit
        }
        if (choice in funcdict):
            funcdict[choice]();
        else:
            print("Command doesn't exist !");
        choice = input("What to do?\n");
    print("Bye!");
        

root = tk.Tk();
root.title("Bored RPG");

app = Application(master=root);
app.mainloop();
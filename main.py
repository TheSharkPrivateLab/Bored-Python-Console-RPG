# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:40:34 2017

@author: ccameron
"""
from tkinter import Tk, Frame, StringVar, Canvas, Message, Button, Label, RAISED, FLAT, LEFT, TOP
from player import Player, Enemy
from threading import Thread

class Application(Frame):
    def __init__(self, master=None):        
        super().__init__(master);
        
        self.player = Player("Player");
        self.player.assignEnemy(Enemy("Slime", 5, 5, 10));
        
        self.pack();
        self.create_widgets();

    def create_widgets(self):
        self.label_stats_enemy = Label(self, width=20, height=5, text="\nName : {}\n\nHP : {}".format(self.player.enemy.name, self.player.enemy.hp), relief=FLAT, fg='black', command=None)
        self.label_stats_enemy.config(fg='Black', bd=12);
        
        self.label_stats = Label(self, width=20, height=5, text="{} : LVL {} - HP : {}".format(self.player.name, self.player.lvl, self.player.hp), relief=FLAT, fg='black', command=None)
        self.label_stats.config(fg='Black', bd=12);
                
        self.attack = Button(self, width=25, height=5, text="Attack", command=self.player.attack);
        self.block = Button(self, width=25, height=5, text="Block", command=self.player.block);
        self.quit = Button(self, width=25, height=5, text="QUIT", fg="red", command=root.destroy);
        
        self.canvas = Canvas(root, width=700, height=500, bg="white")
        
        self.label_stats.pack(side=TOP, padx=5, pady=5);
        self.label_stats_enemy.pack(side=TOP, padx=5, pady=5);
        self.attack.pack(side=TOP, padx=5, pady=5);
        self.block.pack(side=TOP, padx=5, pady=5);
        self.quit.pack(side=TOP, padx=5, pady=5);
        self.canvas.pack(side=LEFT, padx=5, pady=5);

    def profile(self):
        var = StringVar();
        label = Message( root, textvariable = var, relief = RAISED );
        
        var.set(self.player.name + " : LVL " + str(self.player.lvl));
        label.pack();
 
def main():
    gameState = True;
    while gameState:
        if (app.player.isAlive == False):
            print("Game Over");
            gameState = False;
        else:
            app.label_stats.configure(app.label_stats_enemy, text="{} : LVL {} - HP : {}".format(app.player.name, app.player.lvl, app.player.hp));
            
        if (app.player.enemy):
            app.label_stats_enemy.configure(app.label_stats_enemy, text="\nName : {}\n\nHP : {}".format(app.player.enemy.name, app.player.enemy.hp));
        else:
            app.player.assignEnemy(Enemy("Slime", 5, 5, 10));
root = Tk();
root.title("Bored RPG");
app = Application(master=root);
program = Thread(target=main);
program.start();
app.mainloop();
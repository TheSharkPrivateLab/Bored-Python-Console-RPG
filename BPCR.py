# -*- coding: utf-8 -*-
class Player:
    name = "";
    hp = 50;
    mp = 50;
    atk = 1;
    satk = 1;
    pdef = 1;
    sdef = 1;
    vit = 1;
    enemy = None;
    
    def __init__(self, name):
        self.name = name;
        
    def printName(self):
        return self.name;
    
    def assignEnemy(self, enemy):
        self.enemy = enemy
    
    def attack(self):
        if self.enemy:
            self.enemy.hp -= self.atk;
            print(self.name + " attacks and deals " + str(self.atk) + " point(s) of damages. " + self.enemy.name + " has " + str(self.enemy.hp) + " hp.");
        

class Enemy:
    name = "";
    hp = 0;
    atk = 0;
    
    def __init__(self, name, atk, hp):
        self.name = name;
        self.atk = atk;
        self.hp = hp;
        print(self.name + " apparaît !");
    

def initPlayer():
    p = Player(input("Enter your hero's name :\n"));
    print("Allright " + p.printName() + ", welcome aboard.\n");
    
    p.assignEnemy(Enemy("Slime", 1, 5));
    choice = input("Que faire ?\n");
    while choice != "exit":
        funcdict = {
          "attack": p.attack,
          "exit": exit
        }
        funcdict[choice]()
        choice = input("Que faire ?\n");
    print("Bye\n!");
        
        
def main():
    initPlayer();

main();
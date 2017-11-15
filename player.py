# -*- coding: utf-8 -*-
class Player:
    name = "";
    hp = 50;
    mp = 50;
    atk = 1;
    pdef = 1;
    lvl = 1;
    exp = 0;
    expRequired = 50;
    isAlive = True;
    enemy = None;
    
    def __init__(self, name):
        self.name = name;
        
    def printName(self):
        return self.name;
    
    def assignEnemy(self, enemy):
        self.enemy = enemy
    
    def attack(self):
        if (self.enemy == False):
            self.assignEnemy(Enemy("Auto Slime", 5, 5, 10));
            
        if (self.enemy):
            self.enemy.hp -= self.atk;
            print(self.name + " attacks and deals " + str(self.atk) + " point(s) of damages. " + self.enemy.name + " has " + str(self.enemy.hp) + " hp.");
            if (self.enemy.hp <= 0):
                self.enemy.kill(self);
            else:
                self.takeDamages();
        else:
            print("rip lol");
            
    
    def block(self):
        self.pdef *= 2;
        
    def takeDamages(self):
        damages = self.enemy.atk - self.pdef;
        if damages < 0:
            damages = 0;
        self.hp -= damages;
        if (self.hp <= 0):
            self.hp = 0;
            self.isAlive = False;
                
    def addEXP(self, amount):
        self.exp += amount;
        if (self.exp >= self.expRequired):
            self.lvl += 1;
            self.exp -= self.expRequired;
            print("Level up! ("+ str(self.lvl) + ")");
            
            
        
    def showProfile(self):
        print(self.name + " : LVL " + str(self.lvl) + " " + str(self.exp) + " EXP.");

class Enemy:
    name = "";
    hp = 0;
    atk = 0;
    expReward = 0;
    isAlive = True;
    
    def __init__(self, name, atk, hp, expReward):
        self.name = name;
        self.atk = atk;
        self.hp = hp;
        self.expReward = expReward;
        print(self.name + " appears!");
        
    def kill(self, player):
        self.isAlive = False;
        player.enemy = False;
        print(self.name + " dies! You earn " + str(self.expReward) + " XP.");
        player.addEXP(self.expReward);
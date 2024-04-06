# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:38:58 2024

@author: marve
"""
import pygame, simpleGE, random
""" catch the food 
    Make the chef move
"""
class food(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.sndCoin = simpleGE.Sound("foodprep.mp3")
        self.setImage("food.jpg")
        self.setSize(35, 35)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
            #move to the top of screen 
            self.y = 10
            
            #x is random 0 - screen width 
            self.x = random.randint(0, self.screenWidth)
            
            #dy is random minSpeed to maxSpeed 
            self.dy = random.randint(self.minSpeed, self.maxSpeed)
            
    def checkBounds(self):
            if self.bottom > self.screenHeight: 
                self.reset()
                
    def process(self):
        if self.collidesWith (self.scene.chef):
           self.sndCoin.play()
           self.reset()

                
        
class chef(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Chef.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT): 
            self.x = self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
   
    

        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("kitchen.jpeg")
        
        
        
        self.Food = food(self)
        
        self.food = []
        
        self.chef = chef(self)
        
        for i in range(3):
            self.food.append(food(self))
            
        self.sprites = [self.chef,self.food]
                        
        
        def process(self):
            for food in self.foods:
                if food.collidesWith(self.chef):
                    food.reset()
                    self.sndFood.play()
                   
                
        

                
                       

def main():
       game = Game()
       
       game.start()
                 
                 
                    
                     
if __name__ =="__main__":
    main()
                 
    
    
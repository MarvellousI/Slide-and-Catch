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
                

                
        
class chef(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Chef.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT): 
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
    
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
    
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time Left: 10"
        self.center = (500, 30)

   
    

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("kitchen.jpeg")
        self.sndfood = simpleGE.Sound("foodprep.mp3")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        
        self.lblTime =LblTime()
        self.lblScore = LblScore()
        

        self.chef = chef(self)
        self.food = []
        
        
        for i in range(10):
            self.food.append(food(self))
            
            self.lblScore = LblScore()
            self.lblTime = LblTime()
        
            self.sprites = [self.chef,
                            self.food,
                            self.lblScore, 
                            self.lblTime]
            
                        
        
    def process(self):
        for food in self.food:
            if self.chef.collidesWith(food):
                self.sndfood.play()
        
                print("yes")
                food.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"
            
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
            
        if self.timer.getTimeLeft() < 0: 
           print(f"Final Score: {self.score}")
           self.stop()
                   
class Instructions(simpleGE.Scene):
    def __init__(self, score):
        super().__init__()
        self.setImage("kitchen.jpeg")
        
        self.response = "Play"
        
        self.instructions = simpleGE.MultiLabel()
        self.instructions.textLines = [
        "You are a Chef in a resturant near eiffel tower.",
        "Move with the left and right arrow keys",
        "and catch as much cash as you can",
        "in only ten seconds",
        "",
        "Have fun!"]
        
        self.instructions.center = (320, 240)
        self.instructions.size = (500, 250)
        
        self.prevScore = score
        self.lblScore = simpleGE.Label()
        self.lblScore.text = f"Last score: {self.prevScore}"
        self.lblScore.center = (320, 400)
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play (up)"
        self.btnPlay.center = (100, 400)
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit (down)"
        self.btnQuit.center = (550, 400)
        
        self.sprites = [self.instructions,
                        self.lblScore,
                        self.btnQuit,
                        self.btnPlay]
    def process(self):
        #buttons
           if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop()
           if self.btnPlay.clicked:
            self.response = "Play"
            self.stop()

        #arrow keys
           if self.isKeyPressed(pygame.K_UP):
            self.response = "Play"
            self.stop()
           if self.isKeyPressed(pygame.K_DOWN):
            self.response = "Quit"
            self.stop()

def main():
    
    keepGoing = True
    score = 0
    while keepGoing:
    
        instructions = Instructions(score)
        instructions.start()
                
        if instructions.response == "Play":    
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False
                 
                    
                     
if __name__ =="__main__":
    main()
                 
    
    
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 00:27:15 2023

@author: HP
"""

import time

name=input("Hello What's your Name: ")

print("Welcome! ",name," Let's play the Hangman Game!")

time.sleep(0.5)

print("Rules: ")
time.sleep(2.5)
print("You have to guess the Characters for the word. ")
time.sleep(2.5)
print("Once you input a wrong letter your chance will decrease!")
time.sleep(2.5)

print("Ohk Let's Start Guessing the Word: ")

time.sleep(1.5)

word="beautiful"  #setting the secret

time.sleep(0.5)

print("Hints: ")
time.sleep(2.5)
print("The word consists of of ",len(word)," letters")
time.sleep(2.5)
print("It is used as an adjective for appreciation")
time.sleep(2.5)
guesses=''

turns=len(word)          #no.of times to guess the word

while turns>0:
    c=0
    for i in word:
        if i in guesses:
            print(i,end="")
        else:
            print("_",end="")
            c=c+1
            
    if c==0:
        print('\nYou Won')
        break
    
    guess=input("Guess a Character: ")
    
    guesses += guess
    
    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have ",turns," more chances to guess the word: ")
        
        if turns==0:
            print("You Lose")
            print("The word is ",word)
    
    
    
    
    



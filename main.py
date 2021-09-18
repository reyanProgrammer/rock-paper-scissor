from random import randint

choices = ['rock', 'paper', 'scissor']

guess_computer = choices[randint(0,2)]

guess_player = input("chose rock paper scissor ")

while guess_player!=guess_computer:
    guess_computer = choices[randint(0,2)]

    guess_player = input("chose rock paper scissor retry ")
    
else:
    print("you win good job ")

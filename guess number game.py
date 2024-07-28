import random
def number():
   return str(random.randint(1000,9999))
def guess(secretnum,guessnum):
    bulls=0
    cows=0
    for i in range(4):
      if guessnum[i]==secretnum[i]:
         bulls+=1
      elif guessnum[i] in secretnum:
        cows+=1
    return bulls,cows
def game():
   print("Welcome to Mastermind Game!")
   print("Player 1 set ut secret code with 4digit number")
   player1_num=input("Enter ur number in 4 digit:")
   print("player2 try to guesss playes1 number")
   attempts=0
   while True:
     player2_guess=input("Enter ur guess:")
     attempts+=1
     if player2_guess == player1_num:
       print("Congratulations! player2 guessed number on",attempts,"attempts")
       print("player2 wins")
       break
     else:
       bulls,cows=guess(player1_num,player2_guess)
       print("Incorrect guess.Bulls:",bulls,"cows:",cows)
   print("Now its player2 turn to set number:")
   player2_num=input("Enter ur for digit number:")
   print("player1 guess ur number")
   attempts=0
   while True:
         player1_guess=input("Enter ur guess:")
         attempts+=1
         if player1_guess == player2_num:
            print("Congratulations! player2 guessed number on",attempts,"attempts")
            print("player1 wins")
            break
         else:
           bulls,cows=guess(player2_num,player1_guess)
           print("Incorrect guess.Bulls:",bulls,"cows:",cows)
game()
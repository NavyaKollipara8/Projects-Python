import random
def game():
   choices=["rock","paper","scissor"]
   our_choice=input("Enter ur choice(rock,paper,scissor)").lower()
   computer_choice=random.choice(choices)
   print("Computer chooses:",computer_choice)
   if our_choice==computer_choice:
     print("ITs tie")
   elif (our_choice=="rock" and computer_choice=="scissor") or (our_choice=="paper" and 
      computer_choice=="rock") or (our_choice=="scissor" and computer_choice=="paper"):
      print("You wins!")
   else:
     print("Computer wins")
game()

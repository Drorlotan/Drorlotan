rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
player1 = input('rock, paper, scissors \n')
computer =  random.randint(0,2)
lst = [rock, paper, scissors]

 
if player1 == 'rock':
    if computer == 0:
        print('you chose \n' + lst[0] + '\n' + 'computer chose \n' + lst[computer] + '\n tie')
    elif computer == 1:
        print('you chose \n' + lst[0] + '\n' + 'computer chose \n' + lst[computer] + '\n computer win')
    else:
        print('you chose \n' + lst[0] + '\n' + 'computer chose \n' + lst[computer] +'\n you win')
elif player1 == 'paper':
    if computer == 0:
        print('you chose \n' + lst[1] + '\n' + 'computer chose \n' + lst[computer] +'\n you win')
    elif computer == 1:
        print('you chose \n' + lst[1] + '\n' + 'computer chose \n' + lst[computer] +'\n tie')
    else:
        print('you chose \n' + lst[1] + '\n' + 'computer chose \n' + lst[computer] +'\n computer win')
else:
    if computer == 0:
        print('you chose \n' + lst[2] + '\n' + 'computer chose \n' + lst[computer] +'\n computer win')
    elif computer == 1:
        print('you chose \n' + lst[2] + '\n' + 'computer chose \n' + lst[computer] +'\n you win')
    else:
        print('you chose \n' + lst[2] + '\n' + 'computer chose \n' + lst[computer] +'\n tie')
        
    

import random
print('Welcome to Rock, paper and scisors game \n The rules are : Rock beats scisors, paper beat Rock and scisors beat paper')
choices = ['rock', 'paper', 'scisors']
user_choice = input('Choose one option : Rock or paper or scisors').lower()
computer_choice = random.choice(choices)
print('Computer choice: ', computer_choice)
#Rules
if user_choice == computer_choice:
    print('Same choice, draw')
elif user_choice == 'rock' and computer_choice == 'scisors':
    print('You win')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win')
elif user_choice == 'scisors' and computer_choice == 'paper':
    print('You win')
else:
    print('Wrong choice')

#end of the game



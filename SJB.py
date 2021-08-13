import random

while True:
        print('你会选什么？:')
        choice = str(input())
        choice = choice.lower()

        print("My choice is", choice)

        choices = ['石头', '布', '剪刀']

        computer_choice = random.choice(choices)

        print("Computer choice is", computer_choice)
        if choice in choices: 
            if choice == computer_choice:
                    print('平局')
            if choice == '石头':
                if computer_choice =='布':
                    print('不好意思，你输了。 :(')
                elif computer_choice =='剪刀':
                    print('哇，厉害。 :)')
            if choice == '布':
                if computer_choice =='剪刀':
                    print('不好意思，你输了。 :(')
                elif computer_choice =='石头':
                    print('You win, Congrats! :)')
            if choice == '剪刀':
                if computer_choice == '石头':
                    print('不好意思，你输了。:(')
                elif computer_choice == '布':
                    print ('哇，厉害。:)')
else:
        print('invalid choice, try again')

        print()

        
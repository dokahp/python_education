import random
winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}


default_options = ['rock', 'paper', 'scissors']
file = open('rating.txt', 'r')


def operation(operation, user_name, rating, options):
    if operation == '!exit':
        print("Bye!")
        file.close()
        exit()
    elif operation == '!rating':
        print("Your rating:", rating)
        main(user_name, rating, options)
    elif operation in options:
        rps_game(operation, user_name, rating, options)
    else:
        print("Invalid input")
        main(user_name, rating, options)


def rps_game(user, user_name, rating, options):
    pk_answer = random.choice(options)
    if pk_answer == user:
        print("There is a draw ({})".format(pk_answer))
        rating += 50
    elif pk_answer not in winning_cases[user]:
        print("Sorry, but the computer chose ({})".format(pk_answer))
    else:
        print("Well done. The computer chose ({}) and failed".format(pk_answer))
        rating += 100
    main(user_name, rating, options)


def get_start():
    rating = 0
    name = input("Enter your name:")
    print("Hello,", name)
    options = input().split(',')
    if len(options) <= 1:
        options = default_options
    print("Okay, let's start")
    for line in file:
        a, b = line.split(' ')
        if a != name:
            continue
        elif a == name:
            rating = int(b)
        else:
            rating = 0
    main(name, rating, options)


def main(user_name, rating, options):
    user_operation = input()
    operation(user_operation, user_name, rating, options)


get_start()

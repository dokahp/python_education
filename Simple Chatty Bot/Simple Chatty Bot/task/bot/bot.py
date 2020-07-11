def hello(bot_name, creating_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + creating_year + '.')


def pick_up():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")

def count_numbers():
    print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
    user_number = abs(int(input()))
    count = 0
    while count <= user_number:
        print(count, " !")
        count += 1

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    should_i_stop = False

    while not should_i_stop:
        test_user_input = input()
        if int(test_user_input) != 2:
            print("Please, try again.")

        if int(test_user_input) == 2:
            print("Completed, have a nice day!")
            print("Congratulations, have a nice day!")
            should_i_stop = True
# Основная часть кода
hello("Aid", "2020")
pick_up()
guess_age()
count_numbers()
test()

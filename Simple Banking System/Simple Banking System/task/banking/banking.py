import sqlite3
import random
conn = sqlite3.connect('card.s3db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS card
             (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)''')
conn.commit()


def generate_card():
    global card_number
    str_card_number = "400000" + str(random.randint(1_000_000_000, 9_999_999_999))
    str_card_number = str_card_number[0:15] + "0"
    list_card_number = list(str_card_number)
    for i in range(0, 16, 2):
        if int(list_card_number[i]) >= 5:
            list_card_number[i] = str((int(list_card_number[i]) * 2) - 9)
        elif int(list_card_number[i]) < 5:
            list_card_number[i] = str(int(list_card_number[i]) * 2)
    add_all_numbers = 0
    for i in range(0, 16):
        add_all_numbers = add_all_numbers + int(list_card_number[i])
    if add_all_numbers % 10 == 0:
        card_number = int(str_card_number)
    else:
        for i in range(0, 10):
            if (add_all_numbers + i) % 10 == 0:
                card_number = int(str_card_number[0:15] + str(i))
            else:
                continue
    pin = random.randint(1_000, 9_999)
    card_number = str(card_number)
    pin = str(pin)
    return card_number, pin


def luhn_algorithm(card_number):
    try:
        list_card_number = list(card_number)
        for i in range(0, 16, 2):
            if int(list_card_number[i]) >= 5:
                list_card_number[i] = str((int(list_card_number[i]) * 2) - 9)
            elif int(list_card_number[i]) < 5:
                list_card_number[i] = str(int(list_card_number[i]) * 2)
        add_all_numbers = 0
        for i in range(0, 16):
            add_all_numbers = add_all_numbers + int(list_card_number[i])
        if add_all_numbers % 10 == 0:
            luhn = True
        else:
            luhn = False
    except:
        luhn = False
    return luhn


# Insert a row of data
def insert(card_number, pin):
    card_number = str(card_number)
    pin = str(pin)
    c.execute("INSERT INTO card (number, pin) VALUES ({card}, {pin})".format(card=card_number, pin=pin))
    conn.commit()
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)
    menu()


def select(user_card, user_pin):
    user_card = str(user_card)
    user_pin = str(user_pin)
    for row in c.execute('SELECT * FROM card WHERE number = {ucard} AND pin = {upin}'.format(ucard=user_card,
                                                                                             upin=user_pin)):

        print("You have successfully logged in!")
        print()
        user_card = row[1]
        user_pin = row[2]
        user_menu(user_card, user_pin)
    else:
        print("Wrong card number or PIN")
    menu()


def check_exists_card(transfer_card):
    for row in c.execute('SELECT * FROM card WHERE number = {t_card}'.format(t_card=transfer_card)):
        if transfer_card == row[1]:
            exists = True
        else:
            exists = False
        return exists


def user_menu(u_c, u_p):
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")
    user_input = int(input())
    if user_input == 1:
        balance = 1231254
        for row in c.execute(
                'SELECT * FROM card WHERE number = {ucard} AND pin = {upin}'.format(ucard=u_c, upin=u_p)):
            balance = row[3]
        print("Balance:", balance)
        user_menu(u_c, u_p)
    elif user_input == 2:
        print("Enter income:")
        user_income = int(input())
        for row in c.execute(
                'SELECT * FROM card WHERE number = {ucard} AND pin = {upin}'.format(ucard=u_c, upin=u_p)):
            user_income = user_income + row[3]
        c.execute('UPDATE card SET balance= {user_income} WHERE number = {u_c} and pin={u_p}'.format(user_income=user_income,
                                                                                                     u_c=u_c, u_p=u_p))
        print("Income was added!")
        conn.commit()
        user_menu(u_c, u_p)
    elif user_input == 3:
        print('Transfer')
        print('Enter card number:')
        transfer_card = input()
        if transfer_card == u_c:
            print("You can't transfer money to the same account!")
            user_menu(u_c, u_p)
        else:
            if luhn_algorithm(transfer_card) is False:
                print("Probably you made a mistake in the card number. Please try again!")
                user_menu(u_c,u_p)
            elif luhn_algorithm(transfer_card) is True:
                if check_exists_card(transfer_card) is True:
                    print("Enter how much money you want to transfer:")
                    transfer_money = int(input())
                    for row in c.execute("SELECT * FROM card WHERE number={u_c}".format(u_c=u_c)):
                        balance = row[3]
                        if balance > transfer_money:
                            c.execute(
                                "UPDATE card SET balance={t_m} WHERE number={u_c}".format(t_m=balance - transfer_money,
                                                                                          u_c=u_c))
                            c.execute(
                                "UPDATE card SET balance=balance + {t_b} WHERE number={t_c}".format(t_b=transfer_money,
                                                                                                    t_c=transfer_card))
                            conn.commit()
                            user_menu(u_c, u_p)
                        else:
                            print("Not enough money")
                            user_menu(u_c, u_p)
                else:
                    print("Such a card does not exist.")
                    user_menu(u_c, u_p)

    elif user_input == 4:
        c.execute("DELETE FROM card WHERE number={u_c}".format(u_c=u_c))
        conn.commit()
        print("The account has been closed!")
        menu()
    elif user_input == 5:
        print("You have successfully logged out!")
        print()
        menu()
    elif user_input == 0:
        print("Bye!")
        conn.close()
        exit()


def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")
    menu = int(input())
    if menu == 0:
        print("Bye!")
        conn.close()
        exit()
    elif menu == 1:
        insert(*generate_card())
    elif menu == 2:
        print("Enter your card number:")
        user_card = int(input())
        print("Enter your PIN:")
        user_pin = int(input())
        select(user_card, user_pin)


menu()

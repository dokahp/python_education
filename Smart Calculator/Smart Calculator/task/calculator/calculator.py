from collections import deque
import re
import string
variables = {}


class ConversationToPostfix:
    def __init__(self, infix_len):
        self.stack = []  # для знаков
        self.queue = deque()  # для чисел
        self.infix_len = infix_len
        self.priority = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3}
        self.top = -1

    def is_empty(self):
        return bool(self.stack)  # False - пустой, True - не пустой

    @staticmethod
    def is_digit(char):
        return char.isdigit()

    def is_operator(self, char):
        return char in self.priority

    def higher_priority(self, char):
        try:
            a = self.priority[char]
            b = self.priority[self.stack[-1]]
            return True if a <= b else False
        except KeyError:
            return False

    def infix_to_postfix(self, infix):
        for i in infix:
            if self.is_digit(i) or i.isalpha():  # Если число, то добавляем его в очередь
                self.queue.append(i)
            elif i == '(':  # Если оператор равен левой скобке добавляем ее в стек
                self.stack.append(i)
            elif i == ')':  # Если i правая скобка, то выгружаем стек в очередь, пока не увидим в стеке левую скобку
                while self.stack[-1] != '(':
                    self.queue.append(self.stack.pop())
                self.stack.pop()
            elif self.is_operator(i):  # Если оператор, то в стек, в зависимости от приоритета, отпрвляем в очередь
                if self.is_empty() is False or self.stack[-1] == '(':
                    self.stack.append(i)
                elif self.is_empty():  # Не пустой стек. Проверяем приоритеты
                    if self.priority[i] > self.priority[self.stack[self.top]]:  # Если приоритет выше добавляем в стек
                        self.stack.append(i)
                    else:
                        # Если приоритет равен или меньше
                        while self.is_empty() is True and self.higher_priority(i) and self.stack[-1] != '(':
                            self.queue.append(self.stack.pop())  # то добавляем его в очередь
                        self.stack.append(i)
        for _ in range(len(self.stack)):
            self.queue.append(self.stack.pop())  # После прохода по выражению оставшиеся операторы добавляем в очередь
        return self.queue


def help_command():
    print("""The program calculates the sum of numbers.
The program supports operations +, -, *, /, ^.
And also work with variables!""")


def check_correct_sign(infix):
    for i in range(2,10):
        return False if infix.count('*' * i) > 0 or infix.count('/' * i) > 0 else True


def check_correctness_expression(infix):
    stack = []
    for i in infix:
        if i == '(' or i == ')' and not stack:
            stack.append(i)
        elif i == ')' and stack:
            stack.pop()
    return True if not stack else False  # True, если скобки правильные


def check_binary_operation(infix):  # Преобразовываем множество знаков в один знак
    plus, minus, mult, delenie, i = '+', '-', '*', '/', 10
    while i != 1:
        infix = infix.replace(plus * i, '+')
        if i % 2 == 0:
            infix = infix.replace(minus * i, '+')
        else:
            infix = infix.replace(minus * i, '-')
        i -= 1
    return infix


def give_correct_expression(infix):
    old = ['+', '-', '*', '/', '^', '(', ')']
    new = [' + ', ' - ', ' * ', ' / ', ' ^ ', ' ( ', ' ) ']
    for i in range(len(old)):
        infix = infix.replace(old[i], new[i])  # добавляем пробелы между операторами
    infix = re.sub(r'\s+', ' ', infix)  # Удаляем лишние пробелы, чтобы постфиксная функция работала верно
    return infix

def define_sign_and_calculate(first_digit, second_digit, sign):
    if sign == '+':
        return first_digit + second_digit
    elif sign == '-':
        return first_digit - second_digit
    elif sign == '*':
        return first_digit * second_digit
    elif sign == '/':
        return first_digit / second_digit
    elif sign == '^':
        return first_digit ** second_digit


def calculate_postfix(postfix):
    stack = []
    for char in postfix:
        if char in string.punctuation:
            second = stack.pop()
            first = stack.pop()
            stack.append(define_sign_and_calculate(first, second, char))
        elif char.isdigit:
            stack.append(int(char))
    return int(stack.pop())  # Ответ


def variable_add(user_input):  # Добавляем переменные и их значения в словарь variables
    user_input = user_input.split('=')
    user_input[0], user_input[1] = ''.join(user_input[0].strip()), ''.join(user_input[1].strip())
    if user_input[0].isalpha() is False:
        print("Invalid identifier")
    elif user_input[0].isalpha() and user_input[1].isalpha():
        if user_input[1] in variables.keys():
            variables[user_input[0]] = variables[user_input[1]]
        else:
            print('Unknown variable')
    elif user_input[0].isalpha() and user_input[1].isalpha() is False:
        try:
            variables[user_input[0]] = int(user_input[1])
        except ValueError:
            print('Invalid assignment')


def print_variable_value(user_input):
    if user_input in variables.keys():
        print(variables[user_input])
    else:
        print('Unknown variable')


def is_variable_expression(user_input):
    for char in user_input:
        if char.isalpha():
            return True


def is_digit_expression(user_input):
    for char in user_input:
        if char.isalpha() is False:
            return True


def replace_variable(user_input):
    for i in user_input:
        if i.isalpha():
            if i in variables.keys():
                index = user_input.index(i)
                user_input[index] = i.replace(i, str(variables[i]))
            else:
                print("Unknown variable")
                main()
    return user_input


def main():
    infix = input()
    if len(infix) == 0:
        main()
    elif infix == '/exit':
        print('Bye!')
        exit()
    elif infix == '/help':
        help_command()
        main()
    elif infix[0] == '/' and infix != '/exit' and infix != '/help':
        print('Unknown command')
        main()
    elif infix.count('=') >= 1:  # Если есть знак равно работаем с переменными
        variable_add(infix)
        main()
    elif infix.isalpha():
        print_variable_value(infix)
        main()
    elif infix[1:].isdigit() or infix.isdigit():  # Если пользователь введет одно число и закончит ввод
        print(infix)
        main()
    elif is_variable_expression(infix):
        if check_correctness_expression(infix):  # Проверка правельности скобок
            if check_correct_sign(infix):
                infix = give_correct_expression(check_binary_operation(infix))  # Добавляем пробелы и проверяем на бинарные +-
                replaced_list = replace_variable(infix.split())  # Меняем переменные на их значения
                conv = ConversationToPostfix(len(infix))
                print(calculate_postfix(conv.infix_to_postfix(replaced_list)))
                main()
            else:
                print('Invalid expression')
                main()
        else:
            print('Invalid expression')
            main()
    elif is_digit_expression(infix):
        if check_correctness_expression(infix):  # Проверка правельности скобок
            if check_correct_sign(infix):
                infix = give_correct_expression(check_binary_operation(infix))  # Добавляем пробелы и проверяем на бинарные +-
                conv = ConversationToPostfix(len(infix))
                print(calculate_postfix(conv.infix_to_postfix(infix.split())))
                main()
            else:
                print('Invalid expression')
                main()
        else:
            print('Invalid expression')
            main()


main()

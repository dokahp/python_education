str_test = input()


def check_bracket(expression):
    check_bracket = []
    for i in expression:
        if i == '(':
            check_bracket.append(i)
        elif i == ')':
            if len(check_bracket) > 0:
                check_bracket.pop()
            else:
                return 'ERROR'
    if len(check_bracket) == 0:
        return 'OK'
    else:
        return 'ERROR'


print(check_bracket(str_test))

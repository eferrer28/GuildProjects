#!/usr/bin/python
#

book = {}

def add(name, ph1=None, ph2=None, email=None, addr=None):
    book[name] = [name, ph1, ph2, email, addr]

def show(name):
    print('name: %s' % book[name][0])
    print('phone: %s' % book[name][1])
    print('phone 2: %s' % book[name][2])
    print('email: %s' % book[name][3])
    print('address: %s' % book[name][4])

def delete(name):
    del book[name]

def edit(name, arg, value):
    if arg == 'name': book[name][0] = value
    if arg == 'ph1': book[name][1] = value
    if arg == 'ph2': book[name][2] = value
    if arg == 'email': book[name][3] = value
    if arg == 'addr': book[name][4] = value

def ls_contacts():
    for i in book:
        print(i)


def add_user():
    n = input('Enter a name > ')
    p1 = input('Enter a phone number > ')
    p2 = input('Enter a second phone number > ')
    e = input('Enter an email address > ')
    a = input('Enter an address > ')
   
    add(n,p1,p2,e,a)

    
def delete_user():
    d = input('Who would you like to delete? > ')
    delete(d)


def show_contacts():
    ls_contacts()

def show_name():
    N = input('Enter a name > ')
    show(N)

def edit_contacts():
    N = input('Enter a name > ')
    print('What would you like to change? ')
    C = input('What would you like to change? > ')
    val = input("phone, phone2, email, address? > ")
    if C == 'phone': arg = 'ph1'
    if C == 'phone2': arg = 'ph2'
    if C == 'email': arg = 'email'
    if C == 'address': arg = 'address'

    edit(N, arg, value)



def menu_run():
    while True:
        print('Enter a command. Add, Delete, Edit, Show, List, Quit')
        cmd = input('> ')
        if cmd == 'Add':
            add_user()
        elif cmd == 'Delete':
            delete_user()
        elif cmd == 'Edit':
            edit_contact()
        elif cmd == 'Show':
            show_name()
        elif cmd == 'List':
            show_contacts()
        elif cmd == 'Quit':
             exit()
        else:
            print('try again')


print('Welcome to the address book')
menu_run()

























print('Welcome to the address book')
 


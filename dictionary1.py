# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:26:28 2020

@author: mchoubey
"""
def get_name():
    name = input("Whose details you want:")
    cell = input("Phone number:")
    mail = input("Enter email:")
    return(name, cell, mail)
name = get_name()
def add_contact():
    contacts.append(name)
contacts = {
        'Jason': {
                'phone':'4321',
                'email':'nomail'
                },
        'Mike': {
                'phone':'1234',
                'email':'yesmail'
                }
        }
number = contacts[name]['phone'] 
print(name, 'Phone number is - {}'.format(number))





        

        
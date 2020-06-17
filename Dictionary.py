# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:22:58 2020

@author: mchoubey
"""
contacts = {'Mike':'225522', 'Cilia':'332222'}
print('Mike phone {}.'.format(contacts['Mike']), 'Cilia phone {}.'.format(contacts['Cilia']))
contacts['Vin'] = '555000'
print('Vin phone {}'.format(contacts['Vin']))
print(contacts)
for i in range(0, 10):
    contacts[0] = 'test'
    print (contacts)
    
del contacts['Vin']
print(contacts)
call = {
        'New1':[1, 2, 3, 4, 5],
        'New2':[9, 8 ,7, 5]
        }
for number in call['New1']:
    print(number)
print(call['New1'][0])
print(call['New1'])
print('225522' in contacts.values())


    




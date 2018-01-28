# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:51:10 2018

@author: User Raptorjesus13
"""


print("this is just a randnom test")
print()

coolBeans = {'Director': 'pedro',
             'Department': 'human resouces',
             'Nickname': 'el chino',
             'Hobbies': 'loves cooking'}

name_and_department = (str(coolBeans['Director']) + ' works in the '
                       + str(coolBeans['Department']))

coolBeans['Company'] = 'Ricos Tacos Inc'

#pedro does not find it funny
del(coolBeans['Nickname'])
print("this is just a random revision")
print("this is another cahnge")
print(coolBeans)


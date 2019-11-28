#!/usr/bin/python
# -*- coding: utf-8 -*- 
# @Time : 2019/11/28 9:54 
# @Author : danwuxin 
# @Site :  
# @File : day4.py 
# @Software: PyCharm
classmates = ('1', '2', '3', '4')
print(classmates)

age = 18
if age >= 18:
    print('your age ia', age)
    print('adult')

age = 3;
if age >=18:
    print('your age is',age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age =3;
if age >=18:
    print('your age is', age)
    print('adult')
elif age>=6:
    print('your age is', age)
    print('teenager')
else:
    print('kid')


s=input('birth:')
birth = int(s)
print(birth)

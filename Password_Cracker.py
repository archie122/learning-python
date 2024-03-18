from random import *
from os import system

u_pwd = input("Enter a password : ")
pwd = [1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pw = ""

while pw != u_pwd:
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,17)]
        pw = str(guess_pwd) + str(pw)
        print(pw)
        print("Password : " + pw)
        system('clear')

print("Your password is " + pw)
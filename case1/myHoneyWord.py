#This is a honeyword generator algrithm for CS5435 homework 3
#This file is considering the case where T is the set of the 100
#most common RockYou passwords
#The algrithm used in this honeyword generator is called "Take-a-tail" method.
#It means the tail of the new password is now randomly chosen by the system
#and required when user is entering new password
#Example: propse a password: myPassword
#Append "413" to password
#user then enters his/her new password: myPassword413
#then honeyword generator generates.

#Author: Haiwei Su
#Date: 10/13/2015

import random
import sys
import string
from random import randint

# A short list of high-probability passwords that is used to initialize the
# password list in case no password files are provided. Password source: 
#http://downloads.skullsecurity.org/passwords/rockyou-withcount.txt.bz2.
high_probability_passwords = """
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
nicole
daniel
babygirl
monkey
lovely
jessica
654321
michael
ashley
qwerty
11111
iloveu
000000
michelle
tigger
sunshine
chocolate
password1
soccer
anthony
friends
butterfly
purple
angel
jordan
liverpool
justin
loveme
fuckyou
123123
football
secret
andrea
carlos
jennifer
joshua
bubbles
1234567890
superman
hannah
amanda
loveyou
pretty
basketball
andrew
angels
tweety
flower
playboy
hello
elizabeth
hottie
tinkerbell
charlie
samantha
barbie
chelsea
lovers
teamo
jasmine
brandon
666666
shadow
melissa
eminem
matthew
robert
danielle
forever
family
jonathan
987654321
computer
whatever
dragon
vanessa
cookie
naruto
summer
sweety
spongebob
joseph
junior
softball
taylor
yellow
daniela
lauren
mickey
princesa
"""

def read_password_files(filenames):
    """ 
    Return a list of passwords in all the password listed above (100 total)
    """
    pw_list = [ ]
    lines = high_probability_passwords.split()
    for line in lines:
        pw_list.extend( line.split() )
    return pw_list


def random_with_3_digits(n):
    """
    Return a randomly generated 3 digits appending to exisiting true password
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def append_digits1(list):
    new_pw_list = [ ]
    for pw in list:
        number = random_with_3_digits(3)
        pw = pw + str(number)
        new_pw_list.extend( pw.split() )
    return new_pw_list

def write_into_file1(file_list):
    f = open('true_password', 'w')
    for item in file_list:
        f.write("%s\n" % item)
    f.close()

def write_into_file2(file_list):
    f = open('honey_password', 'w')
    for item in file_list:
        f.write("%s\n" % item)
    f.close()

def append_digits2(string):
    number = random_with_3_digits(3)
    string = string + str(number)
    return string

def make_password(element, user_input):
    """ 
    make a random password like those in given password list
    """
    # start by choosing a random password from the list
    # save its length as k; we'll generate a new password of length k
    #k = len(random.choice(pw_list))
    # create list of all passwords of length k; we'll only use those in model
    ans_list = [ ]
    original_string = element
    for e in range(user_input):
        original_string = append_digits2(original_string)
        ans_list.extend(original_string.split())
        original_string = element
    return ans_list

def generate_passwords(pw_list, number):
    """print n passwords and return list of them """
    ans = [ ]
    for k in range(len(pw_list)):
        element = pw_list[k]
        new_pw = make_password(element, number)
        ans.append(new_pw)
    return ans

def main():
    # get number of passwords desired
    print "Enter number of sweetword you'd like to generate: ",
    sweetword_number = raw_input()
    user_input = int(sweetword_number)
    # read password files
    filenames = sys.argv[2:]           # skip "gen.py" and n   
    pw_list = read_password_files(filenames)
    new_pw_list = append_digits1(pw_list)
    write_into_file1(new_pw_list)
    # generate passwords
    new_passwords = generate_passwords(pw_list, user_input)

    write_into_file2(new_passwords)
    # shuffle their order
    random.shuffle(new_passwords)
    # print if desired
    printing_wanted = True
    # if printing_wanted:
    #     for pw in new_passwords:
    #         print (pw)

# import cProfile
# cProfile.run("main()")

main()
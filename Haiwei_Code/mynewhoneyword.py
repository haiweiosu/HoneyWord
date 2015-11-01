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
#Date: 10/19/2015

import random
import sys
import string
from random import randint
from itertools import izip
import pprint
from collections import Counter



#Set up three thesholds. 
#All three thesholds is dealing with the case where input password contains no numerical digit
#First case: Capitalize random digit in the password
t1 = 0.35
#Second case: Letter map (see detail code below)
t2 = 0.47

#####################################################################################################




def parse_dataset(input_file):
    """
    Parse passwords from dataset and remove frequency count
    If file of form "$FREQUENCY $PASSWORD\n", keep only password
    """
    with open(input_file) as myfile:
        passwords = [line.rstrip('\n') for line in open(input_file)]
        passwords = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in passwords]
    return passwords

def read_password_files(filenames):
    """ 
    Return a list of passwords in all the password listed above (100 total)
    """
    pw_list = [ ]
    lines = high_probability_passwords.split()
    for line in lines:
        pw_list.extend( line.split() )
    return pw_list

# def last_three_is_number(value):
#     temp = value
#     sub = temp[-3:]
#     if sub.isdigit():
#         return True
#     else:
#         return False

def digit_part(value):
    temp = value
    boo = True
    sub = ""
    i = 1
    while i<=len(value) and boo == True:
        if not temp[-i:].isdigit():
            boo = False   
        else:
            sub = temp[-i:]
            i = i+1
            boo = True
    return sub

def random_with_digits(n):
    """
    Return a randomly generated 3 digits appending to exisiting true password
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def append_digits(element, n):
    newelement = element
    number = random_with_digits(n)
    newelement = newelement[:(len(element)-n)] + str(number)
    return newelement

def has_zero_digit(value):
    temp = value
    if temp.isdigit():
        return False
    else:
        return True

index_of_capitalization = []
def action_one(element):
    random_position = randint(0, 100)

    if random_position < len(element):
        if random_position == len(element) - 1:
            word_split = [characters[:random_position] + characters[random_position].upper() for characters in element.split()]
        else :
            word_split = [characters[:random_position] + characters[random_position].upper() + characters[random_position + 1 : len(element)] for characters in element.split()]
    else:
        while random_position >= len(element):
            random_position = randint(0,100)
        if random_position == len(element) - 1:
            word_split = [characters[:random_position] + characters[random_position].upper() for characters in element.split()]
        else :
            word_split = [characters[:random_position] + characters[random_position].upper() + characters[random_position + 1 : len(element)] for characters in element.split()]
    return word_split

def action_two(element):
    letter_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4,'f':5,
                  'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
                   'm':12, 'n':13, 'o':14, 'p':15, 'q':16,'r':17,
                   's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 
                   'y':24,'z':25}

    new_element1 = []
    gap = randint(0,25)
    for char in element:
        old_value = letter_map.get(char)
        new_value = (old_value + gap) % 25

        for key in letter_map.keys():
            if letter_map[key] == new_value:
                new_char = key
                new_element1.append(new_char)
    return new_element1

def action_three(element):
    special_char_map = {'a':'@', 'i':'l', 'l':'1', 'o':'0', 's':'$', 'w': "vv", 'z':'2'}
    num_to_change = randint(0, len(element)-1)
    indices_to_change = []
    for i in range(num_to_change):
        indices_to_change.append(randint(0, len(element)-1))
    new_element1 = []
    for char in element:
        new_element1.append(char)
    for idx in indices_to_change:
        if element[idx] in special_char_map:
            new_element1[idx] = special_char_map[element[idx]]
    return new_element1

def make_password(element, n):
    """ 
    make a random password like those in given password list
    """
    count = 0
    new_element = []
    j = 0
    temp_string = digit_part(element)
    while (j < n):
        if temp_string:
            element1 = append_digits(element, len(temp_string))
            new_element.extend(element1.split())
            j = j+1
        else:
            if has_zero_digit(element):
                p = random.random()         #randomly generate a number and the choice we generate honey word is based on this
                if p < t1:
                    action = "action_1"
                elif p < t1+t2:
                    action = "action_2"
                else:
                    action = "action_3"

                if action == "action_1":    #Capitalize random character in password.  
                    word_split = action_one(element)
                    new_element.extend(word_split)
                    j = j+1
                elif action == "action_2":  #letter map
                    new_element1 = action_two(element)
                    if new_element1 not in new_element:
                        new_element.append("".join(new_element1))
                    else:
                        while new_element1 in new_element:
                            new_element1 = action_two(element)
                        new_element.append("".join(new_element1))
                    j = j+1

                elif action == "action_3":  #randomly generate a leter for each position of password
                    new_element1 = action_three(element)
                    if element == new_element1:
                        new_element1 = action_two(element)
                        if new_element1 not in new_element:
                            new_element.append("".join(new_element1))
                        else:
                            while new_element1 in new_element:
                                new_element1 = action_two(element)
                            new_element.append("".join(new_element1))
                    else:
                        if new_element1 not in new_element:
                            new_element.append("".join(new_element1))
                        else:
                            while new_element1 in new_element:
                                new_element1 = action_three(element)
                            new_element.append("".join(new_element1))
                    j = j+1
    return new_element

def generate_passwords(pw_list, number):
    """ print n passwords for each true password in the new_pw_list and return list of them """
    ans = [ ]
    for k in range(len(pw_list)):
        element = pw_list[k]
        new_pw = make_password(element, number)
        ans.append(new_pw)
    return ans

def write_into_file1(file_list):
    f = open('true_password', 'w')
    for item in file_list:
        f.write("%s\n" % item)
    f.close()

def write_into_file2(file_list1):
    f = open('honey_password', 'w')
    for finallist in file_list1:
        f.write("%s\n" % finallist)
    f.close()

def combine_files (filename1, filename2):
    with open('finaloutput', 'w') as res, open(filename1) as f1, open(filename2) as f2:
        for line1, line2 in zip(f1, f2):
            res.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))

def main():

    # Return early if not enough args
    if len(sys.argv) < 4:
        print "Wrong number of arguments."
        return

    # Parse command-line arguments
    n = int(sys.argv[1])
    inputf = sys.argv[2]
    outputf = sys.argv[3]

    passwords = parse_dataset(inputf) # Parse input file

    # get number of passwords desired
    user_input = n
    user_input = user_input - 1

    # read password files
    write_into_file1(passwords)
    # generate passwords
    new_passwords = generate_passwords(passwords, user_input)
    # combine_files(new_pw_list, new_passwords)

    write_into_file2(new_passwords)
    filename1 = "true_password"
    filename2 = "honey_password"
    combine_files(filename1, filename2)

# import cProfile
# cProfile.run("main()")

main()
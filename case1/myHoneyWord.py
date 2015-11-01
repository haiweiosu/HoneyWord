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
from itertools import izip


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

def write_into_file2(file_list1):
    f = open('honey_password', 'w')
    for finallist in file_list1:
        f.write("%s\n" % finallist)
    f.close()

def combine_files (filename1, filename2):
    with open('finaloutput', 'w') as res, open(filename1) as f1, open(filename2) as f2:
        for line1, line2 in zip(f1, f2):
            res.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))

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
    new_pw_list = append_digits1(passwords)
    write_into_file1(new_pw_list)
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
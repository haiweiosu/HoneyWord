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
    Return a list of passwords in all the password file(s), plus 
    a proportional (according to parameter q) number of "noise" passwords.
    """
    pw_list = [ ]
    for filename in filenames:
        if sys.version_info[0] == 3:
            lines = open(filename,"r",errors='ignore').readlines()
        else:
            lines = open(filename,"r").readlines()
        for line in lines:
            pw_list.extend( line.split() )

    pw_list.extend( noise_list(int(q*len(pw_list))) )
    return pw_list

def random_with_3_digits(n):
    """
    Return a randomly generated 3 digits appending to exisiting true password
    """
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def append_digits(list):
    new_pw_list = [ ]
    for pw in list:
        number = random_with_3_digits(3)
        pw = pw + str(number)
        new_pw_list.extend( pw.split() )
    return new_pw_list

# def syntax(p):
#     """
#     Return True if the last three chars in password p contains 3 digits
#     """
#     global nL, nD, nS
#     L = 0
#     D = 0
#     S = 0
#     for c in p:
#         if c in string.ascii_letters:
#             L += 1
#         elif c in string.digits:
#             D += 1
#         else:
#             S += 1
#     if L >= nL and D >= nD and S >= nS:
#         return True
#     return False

def make_password(new_pw_list):
    """ 
    make a random password like those in given password list
    """
    if random.random() < tn:
        return tough_nut()
    # start by choosing a random password from the list
    # save its length as k; we'll generate a new password of length k
    k = len(random.choice(new_pw_list))
    # create list of all passwords of length k; we'll only use those in model
    L = [ pw for pw in new_pw_list if len(pw) == k ]
    nL = len(L)
    # start answer with the first char of that random password
    # row = index of random password being used 
    row = random.randrange(nL)
    offset =k-3 
    ans = L[row][:offset]           # copy first char of newly-added 3 digits of L[row] 
    j = 1                             # j = len(ans) invariant
    while offset < k:                      # build up ans char by char
        p = random.random()           # randomly decide what to do next, based on p
        # # # here p1 = prob of action 1
        # # #      p2 = prob of action 2
        # # #      p3 = prob of action 3
        # # #      p1 + p2 + p3 = 1.00
        # # if p<p1:
        # #     action = "action_1"
        # # elif p<p1+p2:
        # #     action = "action_2"
        # # else:
        # #     action = "action_3"
        # if action == "action_1":
            # add same char that some random word of length k has in this position
        row = random.randrange(nL)
        ans = ans + L[row][j]
        j = j+1
        offset = offset + 1
        # elif action == "action_2":
        #     # take char in this position of random word with same previous char
        #     LL = [ i for i in range(nL) if L[i][j-1]==ans[-1] ]
        #     row = random.choice(LL)
        #     ans = ans + L[row][j]
        #     j = j + 1
        # elif action == "action_3":
        #     # stick with same row, and copy another character
        #     ans = ans + L[row][j]
        #     j = j + 1
    if (nL > 0 or nD > 0 or nS > 0) and not syntax(ans): 
        return make_password(pw_list)
    return ans

 def generate_passwords( n, pw_list ):
    """ print n passwords and return list of them """
    ans = [ ]
    for t in range( n ):
        new_pw = make_password(new_pw_list)
        ans.append( new_pw )
    return ans

def main():
    # get number of passwords desired
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 10
    # read password files
    filenames = sys.argv[2:]           # skip "gen.py" and n   
    pw_list = read_password_files(filenames)
    # generate passwords
    new_passwords = generate_passwords(n,pw_list)
    # shuffle their order
    random.shuffle(new_passwords)
    # print if desired
    printing_wanted = True
    if printing_wanted:
        for pw in new_passwords:
            print (pw)

# import cProfile
# cProfile.run("main()")

main()







import random
import string
import sys

passwords = []

def parse_dataset(input_file):
    """
    Parse passwords from dataset and remove frequency count
    Expects file of form "$FREQUENCY $PASSWORD\n"
    Warning: Takes ~15 sec as the dataset is huge
    """
    passwords = [line.rstrip('\n') for line in open(input_file)]
    passwords = [line.split()[1] if len(line.split()) > 1 else line.split()[0] for line in passwords]
    return passwords
    print 'Passwords in the input file:', len(passwords)

def append_three(password):
    """
    Append 3 random numbers to password
    """
    return password + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))

def generate_honeyword(password):
    """
    Generate a honeyword by replacing the last 3 characters
    """
    if len(password) <= 3: return append_three(password) # Smaller than 3, just append three random ints
    l = len(password)
    for i in range(3): # Replace last three characters
        if password[l-1-i] in string.letters: char = random.choice(string.letters) # replace letters with letters...
        else: char = str(random.randint(0, 9)) # ...and ints with ints
        password = password[:l-i] + char + password[l+1-i:]
    return password

def generate_n_honeywords(set,n):
    """
    Generate n honeywords for each password
    """
    honeywords = []
    for password in set:
        array = []
        for i in range(n):
            array.append(generate_honeyword(password))
        honeywords.append(array)
    return honeywords

def write_into_file(list, output_file):
    f = open(output_file, 'w+')
    for item in list:
        string = ",".join(item)
        f.write("%s\n" % string)
    f.close()

def main():
    # Return early if not enough args
    if len(sys.argv) < 4:
        print "Wrong number of arguments."
        return

    # Parse command-line arguments
    n = int(sys.argv[1])
    inputf = sys.argv[2]
    outputf = sys.argv[3]

    print 'Parsing the data'
    passwords = parse_dataset(inputf) # Parse input file
    print 'Generating honeywords and writing to file'
    write_into_file(generate_n_honeywords(passwords,n), outputf) # Generate n honeywords and write to output file
    print 'Done'

main()
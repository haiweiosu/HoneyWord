def make_password(element, n):
    """ 
    make a random password like those in given password list
    """
    new_element = []
    j = 0
    while (j < n):
        if last_three_is_number(element):
            element1 = append_digits(element)
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
                    random_position = ranint(0,len(element)-1)
                    element1 = element[:n] + element[random_position].upper() + element[random_position + 1:]
                    new_element.extend(element1.split())
                    j = j+1
                elif action == "action_2":  #letter map
                    letter_map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5,'f':6,
                                  'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
                                   'm':13, 'n':14, 'o':15, 'p':16, 'q':17,'r':18,
                                   's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 
                                   'y':25,'z':26}
                    new_element = ''

                    for char in element:
                        old_value = letter_map.get(char)
                        new_value = old_value+randint(1, 26)
                        if (new_value>26):
                            new_value = new_value-26
                            for key in letter_map.keys():
                                if letter_map[key] == new_value:
                                    new_char = key
                            new_element = new_element.join(new_char)
                        else:
                            for key in letter_map.keys():
                                if letter_map[key] == new_value:
                                    new_char = key
                            new_element = new_element.join(new_char)
                    new_element.extend(element.split())
                    j = j+1

                elif action == "action_3": #randomly generate a leter for each position of password
                    new_element1 = ''
                    for char in element:
                        char = random.choice(string.letters)
                        new_element1 = new_element1.join(char)
                    new_element.extend(new_element1.split())
                    j = j+1
    return new_element
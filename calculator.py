import arithmetic

"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

def check_length(token_list):
    length = len(token_list)
    return length

def two_count_functions(token_list):
    if token_list[0] == "square":
        print arithmetic.square(token_list[1])
    elif token_list[0] == "cube":
        print arithmetic.cube(token_list[1])
    else:
        print "Two few functions. Input again."

def three_count_functions(token_list):
    if token_list[0] == "+":
        print arithmetic.add(token_list[1], token_list[2])
    elif token_list[0] == "-":
        print arithmetic.subtract(token_list[1], token_list[2])
    elif token_list[0] == "*":
        print arithmetic.multiply(token_list[1], token_list[2])
    elif token_list[0] == "/":
        print arithmetic.divide(token_list[1], token_list[2])
    elif token_list[0] == "pow":
        print arithmetic.power(token_list[1], token_list[2])
    elif token_list[0] == "mod":
        print arithmetic.mod(token_list[1], token_list[2])
    else:
        print "Too many functions. Input again."

def main():
    while True:
        # get user input
        user_input = raw_input()
        tokens = user_input.split(" ")
        #print tokens

        # check for numbers
        if tokens[1].isdigit() == False:
            print "Error. Input again."
            continue
        elif tokens[2].isdigit() == False:
            print "Error. Input again."
            continue
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])

        # check length
        if check_length(tokens) == 2:
            two_count_functions(tokens)
        elif check_length(tokens) == 3:
            three_count_functions(tokens)
        elif tokens[0] == "q":
            print "Bye! :)"
            break
        else:
            print "Error. Input again."


if __name__ == '__main__':
    main()

import arithmetic

"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

def check_length(token_list):
    length = len(token_list)
    return length

def two_count_digit_check(token_list):
    if token_list[1].isdigit():
        return True

def three_count_digit_check(token_list):
    if token_list[1].isdigit() and token_list[2].isdigit():
        return True

def two_count_int_convert(token_list):
    token_list[1] = int(token_list[1])
    return token_list[1]

def three_count_int_convert(token_list):
    token_list[1] = int(token_list[1])
    token_list[2] = int(token_list[2])
    return token_list[1], token_list[2]

def two_count_functions(token_list):
    # run two count functions        
    if token_list[0] == "square":
        print arithmetic.square(token_list[1])
    elif token_list[0] == "cube":
        print arithmetic.cube(token_list[1])
    else:
        print "Two few functions. Input again."

def three_count_functions(token_list):
    # run three count functions       
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

def check_operations(operation):
    opsList = ["+", "-", "*", "/", "pow", "mod", "square", "cube"]
    if operation not in opsList:
        return False

def main():
    while True:
        # get user input
        user_input = raw_input()
        tokens = user_input.split(" ")
        #print tokens

        # check for quit
        if tokens[0] == "q":
            print "Bye! :)"
            break

        # check for proper operations
        if check_operations(tokens[0]) == False:
            print "Error: not an operation. Try again."
            continue

        # check length, then check if digits
        if check_length(tokens) == 2:
            if two_count_digit_check(tokens) == True:
                two_count_int_convert(tokens)
                two_count_functions(tokens)
            else: 
                print "Error: input not digits."
        elif check_length(tokens) == 3:
            if three_count_digit_check(tokens) == True:
                three_count_int_convert(tokens)
                three_count_functions(tokens)
            else:
                print "Error: input not digits."
        else:
            print "Error: wrong input length."


if __name__ == '__main__':
    main()

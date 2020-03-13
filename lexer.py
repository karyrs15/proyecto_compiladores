'''
    Autor: Karina Reyes 
'''

import sys
import re
import lex_tokens

# lexer function to tokenize the input code
def lex(input_code, token_expressions):
    # pos tracks position in the input_code
    pos = 0
    tokens = []
    # while is not EOF
    while pos < len(input_code):
        match = None
        # check every token_expression to find which match the input at pos
        for token_expr in token_expressions:
            # recover pattern and tag for every token expression
            pattern, tag = token_expr
            # compile the pattern of token_expr into a regular expression object
            regex = re.compile(pattern)
            # check if input_code matchs the reg expr object starting at pos
            match = regex.match(input_code, pos)
            if match:
                # returns the entire match
                text = match.group(0)
                # if tag is different than None save it, if not, pass it
                if tag:
                    # store token into the list
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            print("Illegal character: %s\n" %(input_code[pos]))
            sys.exit(1)
        # update pos with the index of the end of the entire last match
        pos = match.end(0)
    return tokens

def main():
    if len(sys.argv) != 2:
        print("usage: python3 lexer.py filename")
        sys.exit(1)
    # open file    
    filename = sys.argv[1]
    file = open(filename)
    input_code = file.read()
    file.close()
    # change all file content to lowercase for tokenize
    input_code = input_code.lower()
    # call lexer function
    tokens = lex(input_code, lex_tokens.token_expressions)
    # print list of tokens
    for token in tokens:
        print(token)

if __name__ == '__main__':
    main()
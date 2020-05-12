import sys
import lexer 

def main():
    if len(sys.argv) != 2:
        print("usage: python3 parser.py filename")
        sys.exit(1)
    # open file    
    filename = sys.argv[1]
    file = open(filename)
    input_code = file.read()
    file.close()
    # change all file content to lowercase for tokenize
    input_code = input_code.lower()
    # call lexer function
    tokens = lexer.lex(input_code, lexer.lex_tokens.token_expressions)
    # print list of tokens
    for token in tokens:
        print(token)

if __name__ == '__main__':
    main()
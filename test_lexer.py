import sys
import lexer
import lex_tokens

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("usage: python3 test_lexer.py")
        sys.exit(1)
    for i in range(8):
        # open every file in Examples folder
        filename = ".\Examples\Example" + str(i + 1) + ".pas"
        file = open(filename)
        print("\n\n----- Opening file: " + filename + " -----\n")
        input_code = file.read()
        file.close()
        # change all file content to lowercase for tokenize
        input_code = input_code.lower()
        # call lexer function
        tokens = lexer.lex(input_code, lex_tokens.token_expressions)
        # print list of tokens
        for token in tokens:
            print(token)
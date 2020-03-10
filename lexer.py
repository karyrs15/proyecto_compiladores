import sys
import re
import lex_tokens

def lex(input_code, token_expressions):
    pos = 0
    tokens = []
    while pos < len(input_code):
        match = None
        for token_expr in token_expressions:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(input_code, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write("Illegal character: %s\n" % input_code[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: python3 lexer.py filename")
        sys.exit(1)
    # opern file    
    filename = sys.argv[1]
    file = open(filename)
    input_code = file.read()
    file.close()
    # change all file content to lowercase for tokenize
    input_code = input_code.lower()
    tokens = lex(input_code, lex_tokens.token_expressions)
    # print list of tokens
    for token in tokens:
        print(token)
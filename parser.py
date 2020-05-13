import sys
import csv
import lexer 
import productions_dict

class Action:
    def __init__(self, type, new_item):
        self.type = type
        self.new_item = new_item

def loadActionsTable():
    actions = {}

    for i in range(148):
        actions[str(i)] = {}

    with open("./data/actions.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ' ')
        for row in csvreader:
            # print("item: ", row[0])
            # print("terminal:", row[1])
            # print("action type: ", row[2])
            # print("new item: ", row[3])
            action = Action(row[2], row[3])
            aux = {row[1] : action}
            actions[row[0]].update(aux)

    # print(actions)
    return actions
    
def loadGoToTable():
    gotos = {}

    for i in range(147):
        gotos[str(i)] = {}

    with open("./data/gotos.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ' ')
        for row in csvreader:
            # print("item: ", row[0])
            # print("terminal:", row[1])
            # print("new item: ", row[2])
            aux = {row[1] : row[2]}
            gotos[row[0]].update(aux)

    # print(gotos)
    return gotos

def parse(input):
    # fill actions and gotos
    actions = loadActionsTable()
    gotos = loadGoToTable()
    productions = productions_dict.productions

    # call lexer function
    tokens = lexer.lex(input, lexer.lex_tokens.token_expressions)
    # add $ at the end of input
    tokens.append(("$", "$"))
    # reverse tokens order for easier input reading
    tokens.reverse()

    stack = []
    symbols = []
    accepted = False
    error = False

    stack.append("0")
    
    # print(tokens)
    # ele = tokens.pop()
    # print("Pop: ", ele)
    # print(tokens)
    # print("value: ", ele[1])

    # print(actions["4"]["."].type)
    # print(gotos)

    # print(productions[1])

    # while not(accepted) and not(error):
    #     actual_item = stack[-1]

                

    

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
    parse(input_code)


if __name__ == '__main__':
    main()
    # loadActionsTable()
    # loadGoToTable()
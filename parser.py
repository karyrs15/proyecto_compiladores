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

def display(stack, symbols, token, action):
    print("stack: ", stack)
    print("symbols: ", symbols)
    print("token: ", token)
    print("action: {} {} \n".format(action.type, action.new_item))

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

    # get actual token (the first in the input)
    input_token = str(tokens.pop()[1])
    while not(accepted) and not(error):
        # get stack peek
        actual_item = str(stack[-1])
        
        # get action object
        action = actions.get(actual_item).get(input_token)
        
        display(stack, symbols, input_token, action)
        if action == None:
            error = True
        else:
            if action.type == "shift":
                symbols.append(input_token)
                stack.append(action.new_item)

                # get actual token (the first in the input)
                input_token = str(tokens.pop()[1])
            elif action.type == "reduce":
                prod_length = list(productions[str(action.new_item)])[0]
                prod_head = productions[str(action.new_item)][prod_length]

                for i in range(prod_length):
                    stack.pop()
                    symbols.pop()

                symbols.append(str(prod_head))
                print("Antes de Goto: ")
                display(stack, symbols, input_token, action)

                goto_result = gotos.get(str(stack[-1])).get(str(symbols[-1]))
                stack.append(str(goto_result))

                print("Despues de Goto: ")
                display(stack, symbols, input_token, action)
            elif action.type == "accepted":
                accepted = True

    if accepted:
        print("ACCEPTED")
    else:
        print("ERROR")
                

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
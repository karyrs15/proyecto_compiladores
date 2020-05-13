import sys
import csv
import lexer 

class Action:
    def __init__(self, type, new_item):
        self.tye = type
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

    print(actions)
    
def loadGoToTable():
    gotos = {}

    for i in range(147):
        gotos[str(i)] = {}

    with open("./data/gotos.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        for row in csvreader:
            # print("item: ", row[0])
            # print("terminal:", row[1])
            # print("new item: ", row[2])
            aux = {row[1] : row[2]}
            gotos[row[0]].update(aux)

    print(gotos)

def parse():
    pass

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
    # main()
    loadActionsTable()
    # loadGoToTable()
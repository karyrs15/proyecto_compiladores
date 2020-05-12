'''
    Autor: Karina Reyes 
'''

import lexer

# reserved words
PROGRAM     = 'PROGRAM'
CONST       = 'CONST'
VAR         = 'VAR'
BEGIN       = 'BEGIN'
END         = 'END'
FUNCTION    = 'FUNCTION'
WHILE       = 'WHILE'
DO          = 'DO'
REPEAT      = 'REPEAT'
UNTIL       = 'UNTIL'
FOR         = 'FOR'
TO          = 'TO'
DOWNTO      = 'DOWNTO'
IF          = 'IF'
THEN        = 'THEN'
ELSE        = 'ELSE'
WRITELN     = 'WRITELN'
READLN      = 'READLN'
NOT         = 'NOT'
OR          = 'OR'
DIV         = 'DIV'
MOD         = 'MOD'
AND         = 'AND'

# symbols
ASSIGN      = 'ASSIGN'
COLON       = 'COLON'
SEMI        = 'SEMI'
COMMA       = 'COMMA'
DOT         = 'DOT'
LPAREN      = 'LPAREN'
RPAREN      = 'RPAREN'

# symbols for operations
EQUAL       = 'EQUAL'
NOTEQUAL    = 'NOTEQUAL'
LT          = 'LT'
LEQT        = 'LEQT'
GT          = 'GT'
GEQT        = 'GEQT'
PLUS        = 'PLUS'
MINUS       = 'MINUS'
TIMES       = 'TIMES'
DIVIDE      = 'DIVIDE'

# types
INTEGER     = 'INTEGER'
REAL        = 'REAL'
STRING      = 'STRING'
BOOLEAN     = 'BOOLEAN'
TRUE        = 'TRUE'
FALSE       = 'FALSE'
#E           = 'E'

# identifiers
ID          = 'ID'


# regular expressions for tokens
token_expressions = [
    # ignore blank spaces, tabs or line break
    (r'[ \n\t]+',               None),
    # ignore comments
    (r'//[^\n]*',               None),
    # reserved words
    (r'program',                PROGRAM),
    (r'const',                  CONST),
    (r'var',                    VAR),
    (r'begin',                  BEGIN),
    (r'end',                    END),
    (r'function',               FUNCTION),
    (r'while',                  WHILE),
    (r'repeat',                 REPEAT),
    (r'until',                  UNTIL),
    (r'for',                    FOR),
    (r'to',                     TO),
    (r'downto',                 DOWNTO),
    (r'if',                     IF),
    (r'then',                   THEN),
    (r'else',                   ELSE),
    (r'writeln',                WRITELN),
    (r'readln',                 READLN),
    (r'not',                    NOT),
    (r'or',                     OR),
    (r'div',                    DIV),
    (r'mod',                    MOD),
    (r'and',                    AND),
    # symbols
    (r':=',                     ASSIGN),
    (r'\:',                     COLON),
    (r'\;',                     SEMI),
    (r'\,',                     COMMA),
    (r'\.',                     DOT),
    (r'\(',                     LPAREN),
    (r'\)',                     RPAREN),
    # symbols for operations
    (r'=',                      EQUAL),
    (r'<>',                     NOTEQUAL),
    (r'<=',                     LEQT),
    (r'<',                      LT),
    (r'>=',                     GEQT),
    (r'>',                      GT),
    (r'\+',                     PLUS),
    (r'\-',                     MINUS),
    (r'\*',                     TIMES),
    (r'/',                      DIVIDE),
    # types
    (r'\d+',                    INTEGER),
    (r'\d+\.\d+',               REAL),
    (r'\d+\.\d+',               REAL),
    (r'\'.*?\'',                STRING),
    (r'boolean',                BOOLEAN),
    (r'true',                   TRUE),
    (r'false',                  FALSE),
    # identifiers
    (r'[A-Za-z][A-Za-z0-9_]*',  ID),
]
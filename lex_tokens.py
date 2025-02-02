'''
    Autor: Karina Reyes 
'''

import lexer

# reserved words
PROGRAM     = 'program'
CONST       = 'const'
VAR         = 'var'
BEGIN       = 'begin'
END         = 'end'
FUNCTION    = 'function'
WHILE       = 'while'
DO          = 'do'
REPEAT      = 'repeat'
UNTIL       = 'until'
FOR         = 'for'
TO          = 'to'
DOWNTO      = 'downto'
IF          = 'if'
THEN        = 'then'
ELSE        = 'else'
WRITELN     = 'writeln'
READLN      = 'readln'
NOT         = 'not'
OR          = 'or'
DIV         = 'div'
MOD         = 'mod'
AND         = 'and'

# symbols
ASSIGN      = ':='
COLON       = ':'
SEMI        = ';'
COMMA       = ','
DOT         = '.'
LPAREN      = '('
RPAREN      = ')'

# symbols for operations
EQUAL       = '='
NOTEQUAL    = '<>'
LT          = '<'
LEQT        = '<='
GT          = '>'
GEQT        = '>='
PLUS        = '+'
MINUS       = '-'
TIMES       = '*'
DIVIDE      = '/'

# types
INTEGER     = 'integer'
REAL        = 'real'
STRING      = 'string'
BOOLEAN     = 'boolean'
TRUE        = 'true'
FALSE       = 'false'
#E           = 'E'

# identifiers
ID          = 'identifier'


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
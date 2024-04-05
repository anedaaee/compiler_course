
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'do': 'DO',
    'for': 'FOR',
    'goto': 'GOTO',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'sizeof': 'SIZEOF',
    'struct': 'STRUCT',
    'union': 'UNION',
    'const': 'CONST',
    'volatile': 'VOLATILE',
    'void': 'VOID',
    'char': 'CHAR',
    'short': 'SHORT',
    'int': 'INT',
    'long': 'LONG',
    'float': 'FLOAT',
    'double': 'DOUBLE',
    'signed': 'SIGNED',
    'unsigned': 'UNSIGNED',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'static': 'STATIC',
    'register' : 'REGISTER',
    'extern' : 'EXTERN',
    'typedef' : 'TYPEDEF',
    'auto' : 'AUTO',
    'enum' : 'ENUM'
}
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'FLOAT_NUMBER',
    'STRING',
    'CHARACTER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',
    'ASSIGN',
    'INCREMENT',
    'DECREMENT',
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'MULTIPLY_EQUAL',
    'DIVIDE_EQUAL',
    'MODULO_EQUAL',
    'AND_EQUAL',
    'OR_EQUAL',
    'SHIFT_L',
    'SHIFT_R',
    'AND',
    'OR',
    'XOR',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'SHIFT_L_EQUAL',
    'SHIFT_R_EQUAL',
    'XOR_EQUAL',
    'NOT',
    'BITWISE_NOT',
    'SEMICOLON',
    'LEFT_PAREN',
    'RIGHT_PAREN',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'COMMA',
    'COLON',
    'DOT',
    'ELLIPSIS',
    'COMMENT',
    'INVALID',
    'EMPTY_STRING',
    'QUESTION',
    'ARROW'
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_ASSIGN = r'='
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_MULTIPLY_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='
t_MODULO_EQUAL = r'%='
t_AND_EQUAL = r'&='
t_OR_EQUAL = r'\|='
t_SHIFT_L_EQUAL = r'<<='
t_SHIFT_R_EQUAL = r'>>='
t_XOR_EQUAL = r'\^='
t_SHIFT_L = r'<<'
t_SHIFT_R = r'>>'
t_AND = r'&'
t_OR = r'\|'
t_XOR = r'\^'
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_NOT = r'!'
t_BITWISE_NOT = r'~'
t_SEMICOLON = r';'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_COMMA = r','
t_COLON = r':'
t_DOT = r'\.'
t_ELLIPSIS = r'\.\.\.'
t_EMPTY_STRING = r'\$'
t_ignore = ' \t\n'
t_QUESTION = r'\?'
t_ARROW = r'->'

def t_INVALID(t):
    r'[0-9]+[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_FLOAT_NUMBER(t):
    r'[0-9]*[.][0-9]+'
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t



def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t



def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHARACTER(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

def t_COMMENT(t):
    r'//.*|\/\*.*\*\/'
    pass

def t_error(t):
    print("INVALID TOKEN",t.value[0])
    t.lexer.skip(1)
    return t



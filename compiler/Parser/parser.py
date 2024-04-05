from Parser.treeClasses import *


# <translation-unit> ::= {<external-declaration>}*

def p_translation_unit(p):
    'translation-unit : external-declaration-list'
    # p[0] = TranslationUnit(p[1])
    p[0] = ('translation_unit', p[1])
    pass


def p_external_declaration_list(p):
    '''external-declaration-list : external-declaration external-declaration-list
                                    | lambda'''
    if len(p) == 3:
        p[0] = ('external_declaration_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('external_declaration_list', p[1])
    pass


# def p_external_declaration_list_lambda(p):
#     'external-declaration-list : lambda'
#     pass

# <external-declaration> ::= <function-definition>
# | <declaration>

def p_external_declaration(p):
    '''external-declaration : function-definition'''
    # p[0] = ExternalDeclaration(p[1])
    p[0] = ('external_declaration', p[1])
    pass


# <function-definition> ::= {<declaration-specifier>}* <direct-declarator>
# {<declaration>}* <compound-statement>

def p_function_definition(p):
    'function-definition : declaration-specifier-list direct-declarator declaration-list compound-statement'
    # p[0] = FunctionDefinition(p[1],p[2],p[3],p[4])
    p[0] = ('function_definition', p[1], p[2], p[3], p[4])
    pass


# def p_function_definition(p):
#     'function-definition : declaration-specifier-list declaration compound-statement'
#     pass

def p_declaration_specifier_list(p):
    '''declaration-specifier-list : declaration-specifier declaration-specifier-list
                                    | lambda'''
    if len(p) == 3:
        p[0] = ('declaration_specifier_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('declaration_specifier_list', p[1])
    pass


# def p_declaration_specifier_list_lambda(p):
#     'declaration-specifier-list : lambda'
#     pass

def p_declaration_list(p):
    '''declaration-list : declaration declaration-list
                        | lambda'''
    if len(p) == 3 :
        p[0] = ('declaration_list', p[1], p[2])
    elif len(p) == 2 :
        p[0] = ('declaration_list', p[1])
    pass


# def p_declaration_list_lambda(p):
#     'declaration-list : lambda'
#     pass

# <declaration-specifier> ::= <storage-class-specifier>
# | <type-specifier>
# | <type-qualifier>

def p_declaration_specifier(p):
    '''declaration-specifier : storage-class-specifier
                                | type-specifier
                                | type-qualifier'''

    p[0] = ('declaration_specifier', p[1])
    pass


# <storage-class-specifier> ::= auto
#  | register
# | static
# | extern
# | typedef

def p_storage_class_specifier(p):
    '''storage-class-specifier : AUTO
                                | REGISTER
                                | STATIC
                                | EXTERN
                                | TYPEDEF'''
    p[0] = ('storage_class_specifier', p[1])
    pass


# <type-specifier> ::= void
#  | char
# | int
# | double
# | <struct-or-union-specifier>
#  | <typedef-name>

def p_type_specifier(p):
    '''type-specifier : VOID
                        | CHAR
                        | SHORT
                        | INT
                        | LONG
                        | FLOAT
                        | DOUBLE
                        | struct-or-union-specifier'''
    p[0] = ('type_specifier', p[1])
    pass


# <struct-or-union-specifier> ::= <struct-or-union> <identifier>
# { {<struct-declaration>}+ }
#  | <struct-or-union> { {<struct-declaration>}+ }
#  | <struct-or-union> <identifier>

def p_struct_or_union_specifier(p):
    '''struct-or-union-specifier : struct-or-union IDENTIFIER LEFT_BRACE  struct-declaration struct-declaration-list RIGHT_BRACE
                                    | struct-or-union LEFT_BRACE  struct-declaration struct-declaration-list RIGHT_BRACE
                                    | struct-or-union IDENTIFIER'''
    if len(p) == 7:
            p[0] = ('struct_or_union_specifier', p[1],p[2],p[3],p[4],p[5],p[6])
    elif len(p) == 6:
        p[0] = ('struct_or_union_specifier', p[1],p[2],p[3],p[4],p[5])
    elif len(p) == 3:
        p[0] = ('struct_or_union_specifier', p[1],p[2])
    pass


def p_struct_declaration_list(p):
    '''struct-declaration-list : struct-declaration struct-declaration-list
                                | lambda'''
    if len(p) == 3:
        p[0] = ('struct_declaration_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('struct_declaration_list', p[1])
    pass


# def p_struct_declaration_list_lambda(p):
#     'struct-declaration-list : lambda'
#     pass

# <struct-or-union> ::= struct
#  | union

def p_struct_or_union(p):
    '''struct-or-union : STRUCT
                        | UNION'''
    p[0] = ('struct_or_union', p[1])
    pass


# <struct-declaration> ::= {<specifier-qualifier>}* <struct-declarator-list>

def p_struct_declaration(p):
    'struct-declaration : specifier-qualifier-list struct-declarator-list'
    p[0] = ('struct_declaration', p[1],p[2])
    pass


def p_specifier_qualifier_list(p):
    '''specifier-qualifier-list : specifier-qualifier specifier-qualifier-list
                                | lambda'''
    if len(p) == 3:
        p[0] = ('specifier_qualifier_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('specifier_qualifier_list', p[1])
    pass


# def p_specifier_qualifier_list_lambda(p):
#     'specifier-qualifier-list : lambda'
#     pass

# <specifier-qualifier> ::= <type-specifier>
#  | <type-qualifier>

def p_specifier_qualifier(p):
    '''specifier-qualifier : type-specifier
                            | type-qualifier'''
    p[0] = ('specifier_qualifier', p[1])
    pass


# <struct-declarator-list> ::= <struct-declarator>
#  | <struct-declarator-list> , <struct-declarator>

def p_struct_declarator_list(p):
    '''struct-declarator-list : struct-declarator
                                | struct-declarator-list COMMA struct-declarator'''
    if len(p) == 4:
        p[0] = ('struct_declarator_list', p[1],p[2],p[3])
    elif len(p) == 2:
        p[0] = ('struct_declarator_list', p[1])
    pass


# <struct-declarator> ::= <direct-declarator>
#  | <direct-declarator> : <constant-expression>
#  | : <constant-expression>

def p_struct_declarator(p):
    '''struct-declarator : direct-declarator
                            | direct-declarator COLON constant-expression
                            | COLON constant-expression'''
    if len(p) == 4 :
        p[0] = ('struct_declarator', p[1],p[2],p[3])
    elif len(p) == 3 :
        p[0] = ('struct_declarator', p[1],p[2])
    elif len(p) == 2:
        p[0] = ('struct_declarator', p[1])
    pass


# <type-qualifier> ::= const
#  | volatile

def p_type_qualifier(p):
    '''type-qualifier : CONST
                        | VOLATILE'''
    p[0] = ('type_qualifier', p[1])
    pass


# <direct-declarator> ::= <identifier>
#  | ( <direct-declarator )
# | <direct-declarator> [ {<constant-expression>}? ]
#  | <direct-declarator> ( <parameter-type-list> )
#  | <direct-declarator> ( {<identifier>}* )

def p_direct_declarator(p):
    '''direct-declarator : IDENTIFIER
                            | LEFT_PAREN direct-declarator RIGHT_PAREN
                            | direct-declarator LEFT_BRACKET constant-expression-question RIGHT_BRACKET
                            | direct-declarator LEFT_PAREN parameter-type-list RIGHT_PAREN
                            | direct-declarator LEFT_PAREN  identifier-list RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = ('direct_declarator',p[1],p[2],p[3],p[4])
    elif len(p) == 4:
        p[0] = ('direct_declarator', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('direct_declarator', p[1])
    pass


def p_constant_expression_question(p):
    '''constant-expression-question : constant-expression
                                    | lambda'''
    p[0] = ('constant_expression_question', p[1])
    pass


# def p_constant_expression_question_lambda(p):
#     'constant-expression-question : lambda'
#     pass

def p_identifier_list(p):
    '''identifier-list : IDENTIFIER identifier-list
                        | lambda'''
    if len(p) == 3 :
        p[0] = ('identifier_list', p[1],p[2])
    elif len(p) == 2:
        p[0] = ('identifier_list', p[1])
    pass


# def p_identifier_list_lambda(p):
#     'identifier-list : lambda'
#     pass

# <constant-expression> ::= <logical-or-expression>

def p_constant_expression(p):
    'constant-expression : logical-or-expression'
    p[0] = ('constant_expression', p[1])
    pass


# <logical-or-expression> ::= <logical-and-expression>
#  | <logical-or-expression>
# || <logical-and-expression>

def p_logical_or_expression(p):
    '''logical-or-expression : logical-and-expression
                                | logical-or-expression LOGICAL_OR logical-and-expression'''
    if len(p) == 4 :
        p[0] = ('logical_or_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('logical_or_expression', p[1])
    pass


# <logical-and-expression> ::= <inclusive-or-expression>
#  | <logical-and-expression>
# && <inclusive-or-expression>

def p_logical_and_expression(p):
    '''logical-and-expression : inclusive-or-expression
                                | logical-and-expression LOGICAL_AND inclusive-or-expression'''
    if len(p) == 4 :
        p[0] = ('logical_and_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('logical_and_expression', p[1])
    pass


# <inclusive-or-expression> ::= <exclusive-or-expression>
#  | <inclusive-or-expression>
# | <exclusive-or-expression>
def p_inclusive_or_expression(p):
    '''inclusive-or-expression : exclusive-or-expression
                                | inclusive-or-expression OR exclusive-or-expression'''
    if len(p) == 4 :
        p[0] = ('inclusive_or_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('inclusive_or_expression', p[1])
    pass


# <exclusive-or-expression> ::= <and-expression>
#  | <exclusive-or-expression>
# ^ <and-expression>

def p_exclusive_or_expression(p):
    '''exclusive-or-expression : and-expression
                                    | exclusive-or-expression XOR and-expression'''
    if len(p) == 4 :
        p[0] = ('exclusive_or_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('exclusive_or_expression', p[1])
    pass


# <and-expression> ::= <equality-expression>
#  | <and-expression> & <equality-expression>

def p_and_expression(p):
    '''and-expression : equality-expression
                        | and-expression AND equality-expression'''
    if len(p) == 4 :
        p[0] = ('and_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('and_expression', p[1])
    pass


# <equality-expression> ::= <relational-expression>
#  | <equality-expression> == <relational-expression>
#  | <equality-expression> != <relational-expression>

def p_equality_expression(p):
    '''equality-expression : relational-expression
                            | equality-expression EQUAL relational-expression
                            | equality-expression NOT_EQUAL relational-expression'''
    if len(p) == 4 :
        p[0] = ('equality_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('equality_expression', p[1])
    pass


# <relational-expression> ::= <additive-expression>
#  | <relational-expression> <additive-expression>
#  | <relational-expression> > <additive-expression>
#  | <relational-expression> <= <additive-expression>
#  | <relational-expression> >= <additive-expression>

def p_relational_expression(p):
    '''relational-expression : additive-expression
                            | relational-expression LESS additive-expression
                            | relational-expression GREATER additive-expression
                            | relational-expression LESS_EQUAL additive-expression
                            | relational-expression GREATER_EQUAL additive-expression'''
    if len(p) == 4 :
        p[0] = ('relational_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('relational_expression', p[1])
    pass


# <additive-expression> ::= <multiplicative-expression>
#  | <additive-expression> + <multiplicative-expression>
#  | <additive-expression> - <multiplicative-expression>

def p_additive_expression(p):
    '''additive-expression : multiplicative-expression
                            | additive-expression PLUS multiplicative-expression
                            | additive-expression MINUS multiplicative-expression'''
    if len(p) == 4 :
        p[0] = ('additive_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('additive_expression', p[1])
    pass


# <multiplicative-expression> ::= <cast-expression>
#  | <multiplicative-expression>
# * <cast-expression>
#  | <multiplicative-expression>
# / <cast-expression>

def p_multiplicative_expression(p):
    '''multiplicative-expression : cast-expression
                                | multiplicative-expression MULTIPLY cast-expression
                                | multiplicative-expression DIVIDE cast-expression'''
    if len(p) == 4 :
        p[0] = ('multiplicative_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('multiplicative_expression', p[1])
    pass


# <cast-expression> ::= <unary-expression>
#  | ( <type-name> ) <cast-expression>

def p_cast_expression(p):
    '''cast-expression : unary-expression
                        | LEFT_PAREN type-name RIGHT_PAREN cast-expression'''
    if len(p) == 4 :
        p[0] = ('cast_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('cast_expression', p[1])
    pass


# <unary-expression> ::= <postfix-expression>
# | <unary-operator> <cast-expression>

def p_unary_expression(p):
    '''unary-expression : postfix-expression
                        | unary-operator cast-expression'''
    if len(p) == 3 :
        p[0] = ('unary_expression', p[1],p[2])
    elif len(p) == 2 :
        p[0] = ('unary_expression', p[1])
    pass


# <postfix-expression> ::= <primary-expression>
#  | <postfix-expression> [ <expression> ]
# | <postfix-expression> ( {<assignment-expression>}* )
#  | <postfix-expression> . <identifier>

def p_postfix_expression(p):
    '''postfix-expression : primary-expression
                            | postfix-expression LEFT_BRACE expression RIGHT_BRACE
                            | postfix-expression LEFT_PAREN assignment-expression-list RIGHT_PAREN
                            | postfix-expression  DOT IDENTIFIER'''
    if len(p) == 5 :
        p[0] = ('postfix_expression', p[1],p[2],p[3],p[4])
    elif len(p) == 4 :
        p[0] = ('postfix_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('postfix_expression', p[1])
    pass


def p_assignment_expression_list(p):
    '''assignment-expression-list : assignment-expression assignment-expression-list
                                    | lambda'''
    if len(p) == 3 :
        p[0] = ('assignment_expression_list', p[1],p[2])
    elif len(p) == 2 :
        p[0] = ('assignment_expression_list', p[1])
    pass


# def p_assignment_expression_list_lambda(p):
#     'assignment-expression-list : lambda'
#     pass

# <primary-expression> ::= <identifier>
#  | <constant>
# | <string>
# | ( <expression> )

def p_primary_expression(p):
    '''primary-expression : IDENTIFIER
                            | constant
                            | LEFT_PAREN expression RIGHT_PAREN'''
    if len(p) == 4 :
        p[0] = ('primary_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('primary_expression', p[1])
    pass


# <constant> ::= <integer-constant>
#  | <character-constant>
#  | <floating-constant>

def p_constant(p):
    '''constant : NUMBER
                    | FLOAT_NUMBER
                    | CHARACTER
                    | STRING'''
    p[0] = ('constant', p[1])
    pass


# <expression> ::= <assignment-expression>
#  | <expression> , <assignment-expression>
def p_expression(p):
    '''expression : assignment-expression
                    | expression COMMA assignment-expression'''
    if len(p) == 4 :
        p[0] = ('expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('expression', p[1])
    pass

# <assignment-expression> ::= <logical-or-expression>
# | <unary-expression> = <assignment-expression>

def p_assignment_expression(p):
    '''assignment-expression : logical-or-expression
                                | unary-expression ASSIGN assignment-expression'''
    if len(p) == 4 :
        p[0] = ('assignment_expression', p[1],p[2],p[3])
    elif len(p) == 2 :
        p[0] = ('assignment_expression', p[1])
    pass

# <unary-operator> ::= &
#  | *
# | +
# | -
# | ~
# | !

def p_unary_operator(p):
    '''unary-operator : AND
                        | PLUS
                        | MINUS
                        | MULTIPLY
                        | NOT
                        | BITWISE_NOT'''
    p[0] = ('unary_operator', p[1])
    pass


# <type-name> ::= {<specifier-qualifier>}+ {<direct-abstract-declarator>}?

def p_type_name(p):
    'type-name : specifier-qualifier-list direct-abstract-declarator-question'
    p[0] = ('type_name', p[1],p[2])
    pass


# def p_specifier_qualifier_list(p):
#     '''specifier-qualifier-list : specifier-qualifier specifier-qualifier-list
#                                  | lambda'''
#     pass

# def p_specifier_qualifier_list_lambda(p):
#     'specifier-qualifier-list : lambda'
#     pass

def p_direct_abstract_declarator_question(p):
    '''direct-abstract-declarator-question : direct-abstract-declarator
                                            | lambda'''
    p[0] = ('direct_abstract_declarator_question', p[1])
    pass


# def p_direct_abstract_declarator_question_lambda(p):
#     'direct-abstract-declarator-question : lambda'
#     pass

# <parameter-type-list> ::= <parameter-list>
#  | <parameter-list> , ...

def p_parameter_type_list(p):
    '''parameter-type-list : parameter-list
                            | parameter-list COMMA ELLIPSIS'''
    if len(p) == 4:
        p[0] = ('parameter_type_list', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('parameter_type_list', p[1])
    pass


# <parameter-list> ::= <parameter-declaration>
#  | <parameter-list> , <parameter-declaration>

def p_parameter_list(p):
    '''parameter-list : parameter-declaration
                        | parameter-list COMMA parameter-declaration'''
    if len(p) == 4:
        p[0] = ('parameter_list', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('parameter_list', p[1])
    pass


# <parameter-declaration> ::= {<declaration-specifier>}+ <direct-declarator>
#  | {<declaration-specifier>}+
# <direct-abstract-declarator>
#  | {<declaration-specifier>}+

def p_parameter_declaration(p):
    '''parameter-declaration : declaration-specifier declaration-specifier-list direct-declarator
                                | declaration-specifier declaration-specifier-list direct-abstract-declarator
                                | declaration-specifier declaration-specifier-list'''
    if len(p) == 4:
        p[0] = ('parameter_declaration', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('parameter_declaration', p[1],p[2])
    pass


# <direct-abstract-declarator> ::= ( <direct-abstract-declarator> )
#  | {<direct-abstract-declarator>}?
# [ {<constant-expression>}? ]
#  | {<direct-abstract-declarator>}?
# ( {<parameter-type-list>}? )

def p_direct_abstract_declarator(p):
    '''direct-abstract-declarator : LEFT_PAREN direct-abstract-declarator RIGHT_PAREN
                                    | direct-abstract-declarator-question LEFT_BRACKET constant-expression-question RIGHT_BRACKET
                                    | direct-abstract-declarator-question LEFT_PAREN parameter-type-list-question RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = ('direct_abstract_declarator', p[1], p[2], p[3],p[4])
    elif len(p) == 4:
        p[0] = ('direct_abstract_declarator', p[1],p[2],p[3])
    pass


# def p_direct_abstract_declarator_question(p):
#     '''direct-abstract-declarator-question : direct-abstract-declarator
#                                             | lambda'''
#     pass

# def p_direct_abstract_declarator_question_lambda(p):
#     'direct-abstract-declarator-question : lambda'
#     pass

# def p_constant_expression_question(p):
#     '''constant-expression-question : constant-expression
#                                     | lambda'''
#     pass

# def p_constant_expression_question_lambda(p):
#     'constant-expression-question : lambda'
#     pass

def p_parameter_type_list_question(p):
    '''parameter-type-list-question : parameter-type-list
                                    | lambda'''
    p[0] = ('parameter_type_list_question', p[1])
    pass


# def p_parameter_type_list_question_lambda(p):
#     'parameter-type-list-question : lambda'
#     pass

# <typedef-name> ::= <identifier>

def p_typedef_name(p):
    'typedef-name : IDENTIFIER'
    p[0] = ('typedef_name', p[1])
    pass


# <declaration> ::= {<declaration-specifier>}+ {<init-declarator>}* ;

def p_declaration(p):
    'declaration : declaration-specifier declaration-specifier-list init-declarator-list SEMICOLON'
    p[0] = ('declaration', p[1],p[2],p[3],p[4])
    pass


# def p_declaration_specifier_list(p):
#     '''declaration-specifier-list : declaration-specifier declaration-specifier-list
#                                    | lambda'''
#     pass

# def p_declaration_specifier_list_lambda(p):
#     'declaration-specifier-list : lambda'
#     pass

def p_init_declarator_list(p):
    '''init-declarator-list : init-declarator init-declarator-list
                                | lambda'''

    if len(p) == 4:
        p[0] = ('init_declarator_list', p[1], p[2])
    elif len(p) == 2:
        p[0] = ('init_declarator_list', p[1])
    pass


# def p_init_declarator_list_lambda(p):
#     'init-declarator-list : lambda'
#     pass

# <init-declarator> ::= <direct-declarator>
#  | <direct-declarator> = <initializer>

def p_init_declarator(p):
    '''init-declarator : direct-declarator
                        | direct-declarator ASSIGN initializer'''
    if len(p) == 4:
        p[0] = ('init_declarator', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('init_declarator', p[1])
    pass


# <initializer> ::= <assignment-expression>
#  | { <initializer-list> }
#  | { <initializer-list> , }

def p_initializer(p):
    '''initializer : assignment-expression
                    | LEFT_BRACE initializer-list RIGHT_BRACE
                    | LEFT_BRACE initializer-list RIGHT_BRACE COMMA'''
    if len(p) == 5:
        p[0] = ('initializer', p[1], p[2], p[3],p[5])
    elif len(p) == 4:
        p[0] = ('initializer', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('initializer', p[1])
    pass


# <initializer-list> ::= <initializer>
#  | <initializer-list> , <initializer>

def p_initializer_list(p):
    '''initializer-list : initializer
                        | initializer-list COMMA initializer'''
    if len(p) == 4:
        p[0] = ('initializer_list', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('initializer_list', p[1])
    pass


# <compound-statement> ::= { {<declaration>}* {<statement>}* }

def p_compound_statement(p):
    'compound-statement : LEFT_BRACE declaration-list statement-list RIGHT_BRACE'
    p[0] = ('compound_statement', p[1], p[2], p[3],p[4])
    pass


def p_statement_list(p):
    '''statement-list : statement statement-list
                        | lambda'''
    if len(p) == 4:
        p[0] = ('statement_list', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('statement_list', p[1])
    pass


# def p_statement_list_lambda(p):
#     'statement-list : lambda'
#     pass

# <statement> ::= <expression-statement>
#  | <compound-statement>
#  | <selection-statement>
#  | <iteration-statement>
#  | <jump-statement>

def p_statement(p):
    '''statement : expression-statement
                    | compound-statement
                    | selection-statement
                    | iteration-statement
                    | jump-statement'''

    p[0] = ('statement', p[1])
    pass


# <expression-statement> ::= {<expression>}? ;

def p_expression_statement(p):
    'expression-statement : expression-question SEMICOLON'
    p[0] = ('expression_statement', p[1],p[2])
    pass


def p_expression_question(p):
    '''expression-question : expression
                            | lambda'''
    p[0] = ('expression_question', p[1])
    pass


# def p_expression_question_lambda(p):
#     'expression-question : lambda'
#     pass

# <selection-statement> ::= if ( <expression> ) <statement>
#  | if ( <expression> ) <statement> else <statement>

def p_selection_statement(p):
    '''selection-statement : IF LEFT_PAREN expression RIGHT_PAREN statement
                            | IF LEFT_PAREN expression RIGHT_PAREN statement ELSE statement'''
    if len(p) == 7:
        p[0] = ('selection_statement', p[1], p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 5:
        p[0] = ('selection_statement', p[1], p[2], p[3], p[4])
    pass


# <iteration-statement> ::= while ( <expression> ) <statement>

def p_iteration_statement(p):
    'iteration-statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement'
    p[0] = ('iteration_statement', p[1], p[2], p[3], p[4],p[5])
    pass


# <jump-statement> ::= goto <identifier> ;
#  | continue ;
# | break ;
# | return {<expression>}? ;

def p_jump_statement(p):
    '''jump-statement : GOTO IDENTIFIER SEMICOLON
                        | CONTINUE SEMICOLON
                        | BREAK SEMICOLON
                        | RETURN expression-question SEMICOLON'''
    if len(p) == 4:
        p[0] = ('jump_statement', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('jump_statement', p[1], p[2])
    pass


def p_error(error):
    print('syntax error: ', error)
    pass


def p_lambda(p):
    'lambda : '
    pass

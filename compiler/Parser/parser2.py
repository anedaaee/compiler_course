# <translation-unit> ::= {<external-declaration>}*

def p_start(p):
    print('p_start')
    '''start : translation-unit'''


def p_translation_unit(p):
    '''translation-unit : external-declaration-list'''
    print('p_translation_unit')

def p_external_declaration_list(p):
    '''external-declaration-list : external-declaration external-declaration-list
                                    | lambda'''
    print('p_external_declaration_list')

# <external-declaration> ::= <function-definition>
#                          | <declaration>

def p_external_declaration(p):
    '''external-declaration : function-definition
                            | declaration'''
    print('p_external_declaration')


# <function-definition> ::= {<declaration-specifier>}* <declarator> {<declaration>}* <compound-statement>

def p_function_definition(p):
    '''function-definition : declaration-specifier-list declarator declaration-list compound-statement'''
    print('p_function_definition')

def p_declaration_specifier_list(p):
    '''declaration-specifier-list : declaration-specifier declaration-specifier-list
                                    | lambda'''
    print('p_declaration_specifier_list')

def p_declaration_list(p):
    '''declaration-list : declaration declaration-list
                            | lambda'''
    print('p_declaration_list')


# <declaration-specifier> ::= <storage-class-specifier>
#                           | <type-specifier>
#                           | <type-qualifier>

def p_declaration_specifier(p):
    '''declaration-specifier : storage-class-specifier
                                | type-specifier
                                | type-qualifier'''
    print('p_declaration_specifier')

# <storage-class-specifier> ::= auto
#                             | register
#                             | static
#                             | extern
#                             | typedef


def p_storage_class_specifier(p):
    '''storage-class-specifier : AUTO
                                | REGISTER
                                | STATIC
                                | EXTERN
                                | TYPEDEF'''
    print('p_storage_class_specifier')

# <type-specifier> ::= void
#                    | char
#                    | short
#                    | int
#                    | long
#                    | float
#                    | double
#                    | signed
#                    | unsigned
#                    | <struct-or-union-specifier>
#                    | <enum-specifier>
#                    | <typedef-name>

def p_type_specifier(p):
    '''type-specifier : VOID
                        | CHAR
                        | SHORT
                        | INT
                        | LONG
                        | FLOAT
                        | DOUBLE
                        | SIGNED
                        | UNSIGNED
                        | struct-or-union-specifier
                        | enum-specifier
                        | typedef-name'''
    print('p_type_specifier')


# <struct-or-union-specifier> ::= <struct-or-union> <identifier> { {<struct-declaration>}+ }
#                               | <struct-or-union> { {<struct-declaration>}+ }
#                               | <struct-or-union> <identifier>

def p_struct_or_union_specifier(p):
    '''struct-or-union-specifier : struct-or-union IDENTIFIER struct-declaration struct-declaration-list
                                    | struct-or-union struct-declaration struct-declaration-list
                                    | struct-or-union IDENTIFIER'''
    print('p_struct_or_union_specifier')

def p_struct_declaration_list(p):
    '''struct-declaration-list : struct-declaration struct-declaration-list
                                | lambda'''
    print('p_struct_declaration_list')

# < struct-or-union >: := struct
# | union

def p_struct_or_union(p):
    '''struct-or-union : STRUCT
                        | UNION'''
    print('p_struct_or_union')


# <struct-declaration> ::= {<specifier-qualifier>}* <struct-declarator-list>

def p_struct_declaration(p):
    '''struct-declaration : specifier-qualifier-list struct-declarator-list'''
    print('p_struct_declaration')

def p_specifier_qualifier_list(p):
    '''specifier-qualifier-list : specifier-qualifier specifier-qualifier-list
                                | lambda'''
    print('p_specifier_qualifier_list')

# <specifier-qualifier> ::= <type-specifier>
#                         | <type-qualifier>

def p_specifier_qualifier(p):
    '''specifier-qualifier : type-specifier
                            | type-qualifier'''
    print('p_specifier_qualifier')

# <struct-declarator-list> ::= <struct-declarator>
#                            | <struct-declarator-list> , <struct-declarator>

def p_struct_declarator_list(p):
    '''struct-declarator-list : struct-declarator
                                | struct-declarator-list COMMA struct-declarator'''
    print('p_struct_declarator_list')


# <struct-declarator> ::= <declarator>
#                       | <declarator> : <constant-expression>
#                       | : <constant-expression>

def p_struct_declarator(p):
    '''struct-declarator : declarator
                        | declarator COLON constant-expression
                        | COLON constant-expression'''
    print('p_struct_declarator')


# <declarator> ::= {<pointer>}? <direct-declarator>

#change this
def p_declarator(p):
    '''declarator : pointer-question direct-declarator
                    | type-specifier direct-declarator'''
    print('p_declarator')

def p_pointer_question(p):
    '''pointer-question : pointer
                        | lambda'''
    print('p_pointer_question')

# <pointer> ::= * {<type-qualifier>}* {<pointer>}?

def p_pointer(p):
    '''pointer : MULTIPLY type-qualifier-list pointer-question'''
    print('p_pointer')

def p_type_qualifier_list(p):
    '''type-qualifier-list : type-qualifier type-qualifier-list
                            | lambda'''
    print('p_type_qualifier_list')

# <type-qualifier> ::= const
#                    | volatile

def p_type_qualifier(p):
    '''type-qualifier : CONST
                        | VOLATILE'''
    print('p_type_qualifier')

# <direct-declarator> ::= <identifier>
#                       | ( <declarator> )
#                       | <direct-declarator> [ {<constant-expression>}? ]
#                       | <direct-declarator> ( <parameter-type-list> )
#                       | <direct-declarator> ( {<identifier>}* )

def p_direct_declarator(p):
    '''direct-declarator : IDENTIFIER
                            | LEFT_PAREN declarator RIGHT_PAREN
                            | direct-declarator LEFT_BRACKET constant-expression-question RIGHT_BRACKET
                            | direct-declarator LEFT_PAREN parameter-type-list RIGHT_PAREN
                            | direct-declarator LEFT_PAREN identifier-list RIGHT_PAREN'''
    print('p_direct_declarator')

def p_constant_expression_question(p):
    '''constant-expression-question : constant-expression
                                    | lambda'''
    print('p_constant_expression_question')

def p_identifier_list(p):
    '''identifier-list : IDENTIFIER identifier-list
                        | lambda'''
    print('p_identifier_list')

# <constant-expression> ::= <conditional-expression>

def p_constant_expression(p):
    '''constant-expression : conditional-expression'''
    print('p_constant_expression')

# <conditional-expression> ::= <logical-or-expression>
#                            | <logical-or-expression> ? <expression> : <conditional-expression
def p_conditional_expression(p):
    '''conditional-expression : logical-or-expression
                                | logical-or-expression QUESTION expression COLON conditional-expression'''
    print('p_conditional_expression')

# <logical-or-expression> ::= <logical-and-expression>
#                           | <logical-or-expression> || <logical-and-expression>

def p_logical_or_expression(p):
    '''logical-or-expression : logical-and-expression
                                | logical-or-expression LOGICAL_OR logical-and-expression'''
    print('p_logical_or_expression')

# <logical-and-expression> ::= <inclusive-or-expression>
#                            | <logical-and-expression> && <inclusive-or-expression>

def p_logical_and_expression(p):
    '''logical-and-expression : inclusive-or-expression
                                | logical-and-expression LOGICAL_AND inclusive-or-expression'''
    print('p_logical_and_expression')

# <inclusive-or-expression> ::= <exclusive-or-expression>
#                             | <inclusive-or-expression> | <exclusive-or-expression>

def p_inclusive_or_expression(p):
    '''inclusive-or-expression : exclusive-or-expression
                                | inclusive-or-expression OR exclusive-or-expression'''
    print('p_inclusive_or_expression')

# <exclusive-or-expression> ::= <and-expression>
#                             | <exclusive-or-expression> ^ <and-expression>

def p_exclusive_or_expression(p):
    '''exclusive-or-expression : and-expression
                                | exclusive-or-expression XOR and-expression'''
    print('p_exclusive_or_expression')

# <and-expression> ::= <equality-expression>
#                    | <and-expression> & <equality-expression>

def p_and_expression(p):
    '''and-expression : equality-expression
                        | and-expression AND equality-expression'''
    print('p_and_expression')

# <equality-expression> ::= <relational-expression>
#                         | <equality-expression> == <relational-expression>
#                         | <equality-expression> != <relational-expression>

def p_equality_expression(p):
    '''equality-expression : relational-expression
                            | equality-expression EQUAL relational-expression
                            | equality-expression NOT_EQUAL relational-expression'''
    print('p_equality_expression')

# <relational-expression> ::= <shift-expression>
#                           | <relational-expression> < <shift-expression>
#                           | <relational-expression> > <shift-expression>
#                           | <relational-expression> <= <shift-expression>
#                           | <relational-expression> >= <shift-expression>

def p_relational_expression(p):
    '''relational-expression : shift-expression
                            | relational-expression LESS shift-expression
                            | relational-expression GREATER shift-expression
                            | relational-expression LESS_EQUAL shift-expression
                            | relational-expression GREATER_EQUAL shift-expression'''
    print('p_relational_expression')

# <shift-expression> ::= <additive-expression>
#                      | <shift-expression> << <additive-expression>
#                      | <shift-expression> >> <additive-expression>

def p_shift_expression(p):
    '''shift-expression : additive-expression
                        | shift-expression SHIFT_L additive-expression
                        | shift-expression SHIFT_R additive-expression'''
    print('p_shift_expression')

# <additive-expression> ::= <multiplicative-expression>
#                         | <additive-expression> + <multiplicative-expression>
#                         | <additive-expression> - <multiplicative-expression>

def p_additive_expression(p):
    '''additive-expression : multiplicative-expression
                            | additive-expression PLUS multiplicative-expression
                            | additive-expression MINUS multiplicative-expression'''
    print('p_additive_expression')

# <multiplicative-expression> ::= <cast-expression>
#                               | <multiplicative-expression> * <cast-expression>
#                               | <multiplicative-expression> / <cast-expression>
#                               | <multiplicative-expression> % <cast-expression>

def p_multiplicative_expression(p):
    '''multiplicative-expression : cast-expression
                                | multiplicative-expression MULTIPLY cast-expression
                                | multiplicative-expression DIVIDE cast-expression
                                | multiplicative-expression MODULO cast-expression'''
    print('p_multiplicative_expression')

# <cast-expression> ::= <unary-expression>
#                     | ( <type-name> ) <cast-expression>

def p_cast_expression(p):
    '''cast-expression : unary-expression
                        | LEFT_PAREN type-name RIGHT_PAREN cast-expression'''
    print('p_cast_expression')

# <unary-expression> ::= <postfix-expression>
#                      | ++ <unary-expression>
#                      | -- <unary-expression>
#                      | <unary-operator> <cast-expression>
#                      | sizeof <unary-expression>
#                      | sizeof <type-name>

def p_unary_expression(p):
    '''unary-expression : postfix-expression
                        | INCREMENT unary-expression
                        | DECREMENT unary-expression
                        | unary-operator cast-expression
                        | SIZEOF unary-expression
                        | SIZEOF type-name'''
    print('p_unary_expression')

# <postfix-expression> ::= <primary-expression>
#                        | <postfix-expression> [ <expression> ]
#                        | <postfix-expression> ( {<assignment-expression>}* )
#                        | <postfix-expression> . <identifier>
#                        | <postfix-expression> -> <identifier>
#                        | <postfix-expression> ++
#                        | <postfix-expression> --

def p_postfix_expression(p):
    '''postfix-expression : primary-expression
                            | postfix-expression LEFT_BRACKET expression RIGHT_BRACKET
                            | postfix-expression LEFT_PAREN assignment-expression-list RIGHT_PAREN
                            | postfix-expression DOT IDENTIFIER
                            | postfix-expression ARROW IDENTIFIER
                            | postfix-expression INCREMENT
                            | postfix-expression DECREMENT'''
    print('p_postfix_expression')

def p_assignment_expression_list(p):
    '''assignment-expression-list : assignment-expression assignment-expression-list
                                    | lambda'''
    print('p_assignment_expression_list')

# <primary-expression> ::= <identifier>
#                        | <constant>
#                        | <string>
#                        | ( <expression> )

def p_primary_expression(p):
    '''primary-expression : IDENTIFIER
                            | constant
                            | STRING
                            | CHARACTER
                            | LEFT_PAREN expression RIGHT_PAREN'''
    print('p_primary_expression')

# <constant> ::= <integer-constant>
#              | <character-constant>
#              | <floating-constant>
#              | <enumeration-constant>

def p_constant(p):
    '''constant : NUMBER
                | FLOAT_NUMBER'''
    print('p_constant')

# <expression> ::= <assignment-expression>
#                | <expression> , <assignment-expression>

def p_expression(p):
    '''expression : assignment-expression
                | expression COMMA assignment-expression'''
    print('p_expression')

# <assignment-expression> ::= <conditional-expression>
#                           | <unary-expression> <assignment-operator> <assignment-expression>

def p_assignment_expression(p):
    '''assignment-expression : conditional-expression
                                | unary-expression assignment-operator assignment-expression'''
    print('p_assignment_expression')

# <assignment-operator> ::= =
#                         | *=
#                         | /=
#                         | %=
#                         | +=
#                         | -=
#                         | <<=
#                         | >>=
#                         | &=
#                         | ^=
#                         | |=

def p_assignment_operator(p):
    '''assignment-operator : ASSIGN
                            | MULTIPLY_EQUAL
                            | DIVIDE_EQUAL
                            | MODULO_EQUAL
                            | PLUS_EQUAL
                            | MINUS_EQUAL
                            | SHIFT_L_EQUAL
                            | SHIFT_R_EQUAL
                            | AND_EQUAL
                            | OR_EQUAL
                            | XOR_EQUAL'''
    print('p_assignment_operator')


# <unary-operator> ::= &
#                    | *
#                    | +
#                    | -
#                    | ~
#                    | !

def p_unary_operator(p):
    '''unary-operator : AND
                        | PLUS
                        | MINUS
                        | MULTIPLY
                        | BITWISE_NOT
                        | NOT'''
    print('p_unary_operator')

# <type-name> ::= {<specifier-qualifier>}+ {<abstract-declarator>}?

def p_type_name(p):
    '''type-name : specifier-qualifier specifier-qualifier-list abstract-declarator-question'''
    print('p_type_name')

# def p_specifier_qualifier_list(p):
#     '''specifier-qualifier-list : specifier-qualifier specifier-qualifier-list
#                                 | lambda'''

def p_abstract_declarator_question(p):
    '''abstract-declarator-question : abstract-declarator
                                    | lambda'''
    print('p_abstract_declarator_question')

# <parameter-type-list> ::= <parameter-list>
#                         | <parameter-list> , ...

def p_parameter_type_list(p):
    '''parameter-type-list : parameter-list
                            | parameter-list COMMA ELLIPSIS'''
    print('p_parameter_type_list')

# <parameter-list> ::= <parameter-declaration>
#                    | <parameter-list> , <parameter-declaration>

def p_parameter_list(p):
    '''parameter-list : parameter-declaration
                        | parameter-list COMMA parameter-declaration'''
    print('p_parameter_list')

# <parameter-declaration> ::= {<declaration-specifier>}+ <declarator>
#                           | {<declaration-specifier>}+ <abstract-declarator>
#                           | {<declaration-specifier>}+

def p_parameter_declaration(p):
    '''parameter-declaration : declaration-specifier declaration-specifier-list declarator
                                | declaration-specifier declaration-specifier-list abstract-declarator
                                | declaration-specifier declaration-specifier-list'''
    print('p_parameter_declaration')

# def p_declaration_specifier_list(p):
#     '''declaration-specifier-list : declaration-specifier declaration-specifier-list
#                                     | lambda'''

# <abstract-declarator> ::= <pointer>
#                         | <pointer> <direct-abstract-declarator>
#                         | <direct-abstract-declarator>

def p_abstract_declarator(p):
    '''abstract-declarator : pointer
                            | pointer direct-abstract-declarator
                            | direct-abstract-declarator'''
    print('p_abstract_declarator')

# <direct-abstract-declarator> ::=  ( <abstract-declarator> )
#                                | {<direct-abstract-declarator>}? [ {<constant-expression>}? ]
#                                | {<direct-abstract-declarator>}? ( {<parameter-type-list>}? )

def p_direct_abstract_declarator(p):
    '''direct-abstract-declarator : LEFT_PAREN abstract-declarator RIGHT_PAREN
                                    | direct-abstract-declarator-question LEFT_BRACKET constant-expression RIGHT_BRACKET
                                    | direct-abstract-declarator-question LEFT_PAREN parameter-type-list RIGHT_PAREN'''
    print('p_direct_abstract_declarator')

def p_direct_abstract_declarator_question(p):
    '''direct-abstract-declarator-question : direct-abstract-declarator
                                            | lambda'''
    print('p_direct_abstract_declarator_question')


# <enum-specifier> ::= enum <identifier> { <enumerator-list> }
#                    | enum { <enumerator-list> }
#                    | enum <identifier>

def p_enum_specifier(p):
    '''enum-specifier : ENUM IDENTIFIER LEFT_BRACE enumerator-list RIGHT_BRACE
                        | ENUM LEFT_BRACE enumerator-list RIGHT_BRACE
                        | ENUM IDENTIFIER'''
    print('p_enum_specifier')

# <enumerator-list> ::= <enumerator>
#                     | <enumerator-list> , <enumerator>

def p_enumerator_list(p):
    '''enumerator-list : enumerator
                        | enumerator-list COMMA enumerator'''
    print('p_enumerator_list')

# <enumerator> ::= <identifier>
#                | <identifier> = <constant-expression>

def p_enumerator(p):
    '''enumerator : IDENTIFIER
                    | IDENTIFIER ASSIGN constant-expression'''
    print('p_enumerator')

# <typedef-name> ::= <identifier>

def p_typedef_name(p):
    '''typedef-name : IDENTIFIER'''
    print('p_typedef_name')

# <declaration> ::=  {<declaration-specifier>}+ {<init-declarator>}* ;

def p_declaration(p):
    '''declaration : declaration-specifier declaration-specifier-list init-declarator-list SEMICOLON'''
    print('p_declaration')

def p_init_declarator_list(p):
    '''init-declarator-list : init-declarator init-declarator-list
                            | lambda'''
    print('p_init_declarator_list')


# <init-declarator> ::= <declarator>
#                     | <declarator> = <initializer>

def p_init_declarator(p):
    '''init-declarator : declarator
                        | declarator ASSIGN initializer'''
    print('p_init_declarator')

# <initializer> ::= <assignment-expression>
#                 | { <initializer-list> }
#                 | { <initializer-list> , }

def p_initializer(p):
    '''initializer : assignment-expression
                    | LEFT_BRACE initializer-list RIGHT_BRACE
                    | LEFT_BRACE initializer-list COMMA RIGHT_BRACE'''
    print('p_initializer')

# <initializer-list> ::= <initializer>
#                      | <initializer-list> , <initializer>

def p_initializer_list(p):
    '''initializer-list : initializer
                        | initializer-list COMMA initializer'''
    print('p_initializer_list')

# <compound-statement> ::= { {<declaration>}* {<statement>}* }

def p_compound_statement(p):
    '''compound-statement : LEFT_BRACE declaration-list statement-list RIGHT_BRACE'''
    print('p_compound_statement')

def p_statement_list(p):
    '''statement-list : statement statement-list
                        | lambda'''
    print('p_statement_list')
# <statement> ::= <labeled-statement>
#               | <expression-statement>
#               | <compound-statement>
#               | <selection-statement>
#               | <iteration-statement>
#               | <jump-statement>

def p_statement(p):
    '''statement : labeled-statement
                | expression-statement
                | compound-statement
                | selection-statement
                | iteration-statement
                | jump-statement'''
    print('p_statement')

# <labeled-statement> ::= <identifier> : <statement>
#                       | case <constant-expression> : <statement>
#                       | default : <statement>

def p_labeled_statement(p):
    '''labeled-statement : IDENTIFIER COLON statement
                            | CASE COLON statement
                            | DEFAULT COLON statement'''
    print('p_labeled_statement')

# <expression-statement> ::= {<expression>}? ;

def p_expression_statement(p):
    '''expression-statement : expression-question SEMICOLON'''
    print('p_expression_statement')

def p_expression_question(p):
    '''expression-question : expression
                            | lambda'''
    print('p_expression_question')

# <selection-statement> ::= if ( <expression> ) <statement>
#                         | if ( <expression> ) <statement> else <statement>
#                         | switch ( <expression> ) <statement>

def p_selection_statement(p):
    '''selection-statement : IF LEFT_PAREN expression RIGHT_PAREN statement
                            | IF LEFT_PAREN expression RIGHT_PAREN statement ELSE statement
                            | SWITCH LEFT_PAREN expression RIGHT_PAREN statement'''
    print('p_selection_statement')

# <iteration-statement> ::= while ( <expression> ) <statement>
#                         | do <statement> while ( <expression> ) ;
#                         | for ( {<expression>}? ; {<expression>}? ; {<expression>}? ) <statement>

def p_iteration_statement(p):
    '''iteration-statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement
                            | DO statement WHILE LEFT_PAREN expression RIGHT_PAREN SEMICOLON
                            | FOR LEFT_PAREN expression-question SEMICOLON expression-question SEMICOLON expression-question RIGHT_PAREN statement'''
    print('p_iteration_statement')


# <jump-statement> ::= goto <identifier> ;
#                    | continue ;
#                    | break ;
#                    | return {<expression>}? ;

def p_jump_statement(p):
    '''jump-statement : GOTO IDENTIFIER SEMICOLON
                        | CONTINUE SEMICOLON
                        | BREAK SEMICOLON
                        | RETURN expression-question SEMICOLON'''
    print('p_jump_statement')


def p_error(error):
    print('\033[91m syntax error: ', error,'\033[0m')
    pass


def p_lambda(p):
    'lambda : '
    pass

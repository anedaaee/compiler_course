precedence = (
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'ASSIGN', 'NOT_EQUAL', 'LESS', 'LESS_EQUAL', 'GREATER', 'GREATER_EQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
    )


def p_translation_unit(p):
    '''translation-unit : external-declaration-list'''
    p[0] = ('translation-unit', p[1])


def p_external_declaration_list(p):
    '''external-declaration-list : external-declaration external-declaration-list
                                 | lambda'''
    if len(p) == 3:
        p[0] = ('external-declaration-list', p[1], p[2])
    else:
        p[0] = ('external-declaration-list', p[1])


def p_external_declaration(p):
    '''external-declaration : function-definition'''
    p[0] = ('external-declaration', p[1])


def p_function_definition(p):
    'function-definition :  declaration-specifier-list direct-declarator declaration-list compound-statement '
    p[0] = ('function-definition', p[1], p[2], p[3], p[4])


def p_declaration_specifier_list(p):
    '''declaration-specifier-list : declaration-specifier declaration-specifier-list
                                  | lambda'''
    if len(p) == 3:
        p[0] = ('declaration-specifier-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_declaration_list(p):
    '''declaration-list : declaration declaration-list
                        | lambda'''
    if len(p) == 3:
        p[0] = ('declaration-list', p[1], p[2],)
    else:
        p[0] = p[1]


def p_declaration_specifier(p):
    '''declaration-specifier : storage-class-specifier
                              | type-specifier
                              | type-qualifier'''
    p[0] = ('declaration-specifier', p[1])


def p_storage_class_specifier(p):
    '''storage-class-specifier : AUTO
                               | REGISTER
                               | STATIC
                               | EXTERN
                               | TYPEDEF '''
    p[0] = ('storage-class-specifier', p[1])


def p_type_specifier(p):
    '''type-specifier : VOID
                      | FLOAT
                      | CHAR
                      | INT
                      | DOUBLE
                      | struct-or-union-specifier
                      '''
    p[0] = ('type-specifier', p[1])
    # print(p[0])


def p_struct_or_union_specifier(p):
    '''struct-or-union-specifier : struct-or-union IDENTIFIER LEFT_BRACE struct-declaration struct-declaration-list RIGHT_BRACE
                                 | struct-or-union LEFT_BRACE struct-declaration struct-declaration-list RIGHT_BRACE
                                 | struct-or-union IDENTIFIER '''
    if len(p) == 7:
        p[0] = ('struct-or-union-specifier', p[1], p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 6:
        p[0] = ('struct-or-union-specifier', p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = ('struct-or-union-specifier', p[1], p[2])


def p_struct_declaration_list(p):
    '''struct-declaration-list : specifier-qualifier-list struct-declaration-list
                               | lambda'''
    if len(p) == 3:
        p[0] = ('struct-declaration-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_struct_or_union(p):
    '''struct-or-union : STRUCT
                       | UNION'''
    p[0] = ('struct-or-union', p[1])


def p_struct_declaration(p):
    'struct-declaration : specifier-qualifier-list struct-declarator-list'
    p[0] = ('struct-declaration', p[1], p[2])


def p_struct_declarator_list(p):
    '''struct-declarator-list : struct-declarator
                              | struct-declarator-list COMMA struct-declarator '''
    if len(p) == 3:
        p[0] = ('struct-declarator-list', p[1], p[2], p[3])
    else:
        p[0] = ('struct-declarator-list', p[1])


def p_struct_declarator(p):
    '''struct-declarator : direct-declarator
                          | direct-declarator COLON constant-expression
                          | COLON constant-expression '''
    if len(p) == 3:
        p[0] = ('struct-declarator', p[1], p[2], p[3])
    elif len(p) == 2:
        p[0] = ('struct-declarator', p[1], p[2])
    else:
        p[0] = ('struct-declarator', p[1])


def p_specifier_qualifier_list(p):
    '''specifier-qualifier-list : specifier-qualifier specifier-qualifier-list
                                | lambda'''
    if len(p) == 3:
        p[0] = ('specifier-qualifier-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_specifier_qualifier(p):
    '''specifier-qualifier : type-specifier
                            | type-qualifier'''
    p[0] = ('specifier-qualifier', p[1])


def p_type_qualifier(p):
    '''type-qualifier : CONST
                      | VOLATILE'''

    p[0] = ('type-qualifier', p[1])


def p_direct_declarator(p):
    '''direct-declarator : IDENTIFIER
                         | LEFT_PAREN direct-declarator RIGHT_PAREN
                         | direct-declarator LEFT_BRACKET constant-expression-list RIGHT_BRACKET
                         | direct-declarator LEFT_PAREN parameter-type-list RIGHT_PAREN
                         | direct-declarator LEFT_PAREN identifier-list RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = ('direct-declarator',p[1],p[2],p[3],p[4])
    elif len(p) == 4:
        p[0] = ('direct-declarator',p[1],p[2],p[3])
    elif len(p) == 2:
        p[0] = ('direct-declarator', p[1])


def p_identifier_list(p):
    '''identifier-list : IDENTIFIER identifier-list
                       | lambda'''
    if len(p) == 3:
        p[0] = ('identifier-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_constant_expression_list(p):
    '''constant-expression-list : constant-expression
                                | lambda'''

    p[0] = ('constant-expression-list', p[1])


def p_constant_expression(p):
    'constant-expression : logical-or-expression'
    p[0] = ('constant-expression', p[1])


def p_logical_or_expression(p):
    '''logical-or-expression : logical-and-expression
                             | logical-or-expression LOGICAL_OR logical-and-expression'''
    if len(p) == 4:
        p[0] = ('logical-or-expression', p[1], p[2], p[3])
    else:
        p[0] = ('logical-or-expression', p[1])


def p_logical_and_expression(p):
    '''logical-and-expression : inclusive-or-expression
                              | logical-and-expression LOGICAL_AND inclusive-or-expression'''
    if len(p) == 4:
        p[0] = ('logical-and-expression', p[1], p[2], p[3])
    else:
        p[0] = ('logical-and-expression', p[1])


def p_inclusive_or_expression(p):
    '''inclusive-or-expression : exclusive-or-expression
                               | inclusive-or-expression OR exclusive-or-expression '''
    if len(p) == 4:
        p[0] = ('inclusive-or-expression', p[1], p[2], p[3])
    else:
        p[0] = ('inclusive-or-expression', p[1])


def p_exclusive_or_expression(p):
    '''exclusive-or-expression : and-expression
                               | exclusive-or-expression XOR and-expression '''
    if len(p) == 4:
        p[0] = ('exclusive-or-expression', p[1], p[2], p[3])
    else:
        p[0] = ('exclusive-or-expression', p[1])


def p_and_expression(p):
    '''and-expression : equality-expression
                      | and-expression XOR equality-expression'''
    if len(p) == 4:
        p[0] = ('and-expression', p[1], p[2], p[3])
    else:
        p[0] = ('and-expression', p[1])


def p_equality_expression(p):
    '''equality-expression : relational-expression
                           | equality-expression EQUAL relational-expression
                           | equality-expression NOT_EQUAL relational-expression'''
    if len(p) == 4:
        p[0] = ('equality-expression', p[1], p[2], p[3])
    else:
        p[0] = ('equality-expression', p[1])


def p_relational_expression(p):
    '''relational-expression : additive-expression
                             | relational-expression LESS additive-expression
                             | relational-expression GREATER additive-expression
                             | relational-expression LESS_EQUAL additive-expression
                             | relational-expression GREATER_EQUAL additive-expression'''
    if len(p) == 4:
        p[0] = ('relational-expression', p[1], p[2], p[3])
    else:
        p[0] = ('relational-expression', p[1])


def p_additive_expression(p):
    '''additive-expression : multiplicative-expression
                           | additive-expression PLUS multiplicative-expression
                           | additive-expression MINUS multiplicative-expression'''
    if len(p) == 4:
        p[0] = ('additive-expression', p[1], p[2], p[3])
    else:
        p[0] = ('additive-expression', p[1])


def p_multiplicative_expression(p):
    '''multiplicative-expression : cast-expression
                                 | multiplicative-expression MULTIPLY cast-expression
                                 | multiplicative-expression DIVIDE cast-expression  '''
    if len(p) == 4:
        p[0] = ('multiplicative-expression', p[1], p[2], p[3])
    else:
        p[0] = ('multiplicative-expression', p[1])


def p_cast_expression(p):
    '''cast-expression : unary-expression
                       | LEFT_PAREN type-name RIGHT_PAREN cast-expression'''
    if len(p) == 5:
        p[0] = ('cast-expression', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('cast-expression', p[1])

def p_unary_expression(p):
    '''unary-expression : postfix-expression
                        | unary-operator cast-expression  '''
    if len(p) == 3:
        p[0] = ('unary-expression', p[1], p[2])
    else:
        p[0] = ('unary-expression', p[1])


def p_postfix_expression(p):
    '''postfix-expression : primary-expression
                          | postfix-expression LEFT_BRACKET expression RIGHT_BRACKET
                          | postfix-expression LEFT_PAREN assignment-expression-list RIGHT_PAREN
                          | postfix-expression DOT IDENTIFIER'''
    if len(p) == 5:
        p[0] = ('postfix-expression', p[1], p[2], p[3], p[4])
    elif len(p) == 4:
        p[0] = ('postfix-expression', p[1], p[2], p[3])
    else:
        p[0] = ('postfix-expression', p[1])


def p_assignment_expression_list(p):
    '''assignment-expression-list : assignment-expression assignment-expression-list
                                  | lambda'''
    if len(p) == 3:
        p[0] = ('assignment-expression-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_primary_expression(p):
    '''primary-expression : IDENTIFIER
                          | constant
                          | STRING
                          | LEFT_PAREN expression RIGHT_PAREN '''
    if len(p) == 4:
        p[0] = ('primary-expression', p[1], p[2], p[3])
    else:
        p[0] = ('primary-expression', p[1])


def p_constant(p):
    '''constant : NUMBER
                | CHARACTER
                | FLOAT_NUMBER '''
    p[0] = ('constant', p[1])


def p_expression(p):
    '''expression : assignment-expression
                  | expression COMMA assignment-expression '''
    if len(p) == 4:
        p[0] = ('expression', p[1], p[2], p[3])
    else:
        p[0] = ('expression', p[1])


def p_assignment_expression(p):
    '''assignment-expression : logical-or-expression
                             | unary-expression ASSIGN assignment-expression '''
    if len(p) == 4:
        p[0] = ('assignment-expression', p[1], p[2], p[3])
    else:
        p[0] = ('initializer', p[1])


def p_unary_operator(p):
    '''unary-operator : LOGICAL_AND
                      | MULTIPLY
                      | PLUS
                      | MINUS
                      | BITWISE_NOT
                      | NOT'''
    p[0] = ('unary-operator', p[1])


def p_type_name(p):
    'type-name : specifier-qualifier specifier-qualifier-list direct-abstract-declarator-list'
    p[0] = ('type-name', p[1], p[2], p[3])


def p_direct_abstract_declarator_list(p):
    '''direct-abstract-declarator-list : direct-abstract-declarator
                                       | lambda'''

    p[0] = ('direct-abstract-declarator-list', p[1])


def p_parameter_type_list(p):
    '''parameter-type-list : parameter-list
                           | parameter-list COMMA ELLIPSIS'''
    if len(p) == 4:
        p[0] = ('parameter-type-list', p[1], p[2], p[3])
    else:
        p[0] = ('parameter-type-list', p[1])


def p_parameter_list(p):
    '''parameter-list : parameter-declaration
                      | parameter-list COMMA parameter-declaration '''
    if len(p) == 4:
        p[0] = ('parameter-list', p[1], p[2] ,p[3])


def p_parameter_declaration(p):
    '''parameter-declaration : declaration-specifier declaration-specifier-list direct-declarator
                             | declaration-specifier declaration-specifier-list direct-abstract-declarator
                             | declaration-specifier declaration-specifier-list '''
    if len(p) == 4:
        p[0] = ('parameter-declaration', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('parameter-declaration', p[1], p[2])


def p_direct_abstract_declarator(p):
    '''direct-abstract-declarator : LEFT_PAREN direct-abstract-declarator RIGHT_PAREN
                                    | direct-abstract-declarator-list LEFT_BRACKET constant-expression-list RIGHT_BRACKET
                                    | direct-abstract-declarator-list LEFT_PAREN parameter-type-list-1 RIGHT_PAREN'''
    if len(p) == 5:
        p[0] = ('direct-abstract-declarator', p[1], p[2], p[3], p[4])
    elif len(p) == 3:
        p[0] = ('parameter-declaration', p[1], p[2], p[3])


def p_parameter_type_list_1(p):
    '''parameter-type-list-1 : parameter-type-list
                                | lambda'''
    p[0] = ('parameter-type-list-1', p[1])


def p_declaration(p):
    '''declaration : declaration-specifier declaration-specifier-list init-declarator-list SEMICOLON'''
    p[0] = ('declaration', p[1], p[2], p[3], p[4])


def p_init_declarator_list(p):
    '''init-declarator-list : init-declarator init-declarator-list
                            | lambda'''
    if len(p) == 3:
        p[0] = ('init-declarator-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_init_declarator(p):
    '''init-declarator : direct-declarator
                       | direct-declarator ASSIGN initializer '''
    if len(p) == 4:
        p[0] = ('init-declarator', p[1], p[2],p[3])
    elif len(p) == 2:
        p[0] = ('init-declarator', p[1])


def p_initializer(p):
    '''initializer : assignment-expression
                   | LEFT_BRACE initializer-list RIGHT_BRACE
                   | LEFT_BRACE initializer-list COMMA RIGHT_BRACE'''
    if len(p) == 5:
        p[0] = ('initializer', p[1], p[2], p[3], p[4])
    elif len(p) == 4:
        p[0] = ('initializer', p[1], p[2], p[3])
    else:
        p[0] = ('initializer', p[1])


def p_initializer_list(p):
    '''initializer-list : initializer
                        | initializer-list COMMA initializer'''
    if len(p) == 4:
        p[0] = ('initializer-list', p[1], p[2], p[3])
    else:
        p[0] = ('initializer-list', p[1])


def p_compound_statement(p):
    '''compound-statement : LEFT_BRACE declaration-list  statement-list RIGHT_BRACE'''
    p[0] = ('compound-statement', p[1], p[2], p[3], p[4])


def p_statement_list(p):
    '''statement-list : statement statement-list
                      | lambda'''
    if len(p) == 3:
        p[0] = ('statement-list', p[1], p[2])
    else:
        p[0] = p[1]


def p_statement(p):
    '''statement : expression-statement
                 | compound-statement
                 | selection-statement
                 | iteration-statement
                 | jump-statement'''
    p[0] = ('statement', p[1])


def p_expression_statement(p):
    '''expression-statement : expression SEMICOLON
                            | SEMICOLON'''
    if len(p) == 2:
        p[0] = ('expression-statement', p[1], p[2])
    else:
        p[0] = ('expression-statement', p[1])


def p_selection_statement(p):
    '''selection-statement : IF LEFT_PAREN expression RIGHT_PAREN statement
                           | IF LEFT_PAREN expression RIGHT_PAREN statement ELSE statement'''
    if len(p) == 8:
        p[0] = ('selection-statement', p[1], p[2], p[3], p[4], p[5], p[6], p[7])
    elif len(p) == 6:
        p[0] = ('selection-statement', p[1], p[2], p[3], p[4], p[5])


def p_iteration_statement(p):
    'iteration-statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement'
    p[0] = ('iteration-statement', p[1], p[2], p[3], p[4], p[5])


def p_jump_statement(p):
    '''jump-statement : GOTO IDENTIFIER SEMICOLON
                      | CONTINUE SEMICOLON
                      | BREAK SEMICOLON
                      | RETURN expression-list SEMICOLON '''
    if len(p) == 4:
        p[0] = ('jump-statement', p[1], p[2], p[3])
    elif len(p) == 3:
        p[0] = ('jump-statement', p[1], p[2])
    else:
        p[0] = ('jump-statement', p[1], p[2])


def p_expression_list(p):
    '''expression-list : expression
                       | lambda'''
    p[0] = ('expression-list', p[1])


def p_lambda(p):
    'lambda : '
    pass


def p_error(error):
    if error:
        print(f"Syntax error at token' {error.value} , line {error.lineno}")

    else:
        print("Syntax error")


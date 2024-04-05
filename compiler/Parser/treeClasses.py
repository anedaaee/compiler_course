class Node:
    def __init__(self, *args):
        pass


class TranslationUnit(Node):
    def __init__(self, external_declaration_list):
        super().__init__(external_declaration_list)
        self.external_declaration_list = external_declaration_list


class ExternalDeclarationListTwoInput(Node):
    def __init__(self, external_declaration, external_declaration_list):
        super().__init__(external_declaration, external_declaration_list)
        self.external_declaration = external_declaration
        self.external_declaration_list = external_declaration_list


class ExternalDeclarationListOneInput(Node):
    def __init__(self, lambdaRule):
        super().__init__(lambdaRule)
        self.lambdaRule = lambdaRule


class ExternalDeclaration(Node):
    def __init__(self, declaration):
        super().__init__(declaration)
        self.declaration = declaration

class FunctionDefinition(Node):
    def __init__(self,declaration_specifier_list,direct_declarator,declaration_list,compound_statement):
        super().__init__(declaration_specifier_list,direct_declarator,declaration_list,compound_statement)
        self.declaration_specifier_list = declaration_specifier_list
        self.direct_declarator = direct_declarator
        self.declaration_list = declaration_list
        self.compound_statement = compound_statement

class DeclarationSpecifierList(Node):
    def __init__(self,declaration_specifier , declaration_specifier_list):
        super().__init__(declaration_specifier,declaration_specifier_list)


# class DeclarationSpecifierList(Node):
#     def __init__(self):
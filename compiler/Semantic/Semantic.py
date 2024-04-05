import uuid

class Semantic:
    def __init__(self,ast):
        self.ast = ast
        self.stack = {}
        self.SymbolTable = []
        self.memory = 0
        self.code = ''
        self.variableDef = ''
    def iterate(self, tuple_value, whilePointer='', endWhilePointer=''):
        try:

            if (tuple_value[0] == 'assignment-expression'):
                self.handleAssignmentExpression(tuple_value)
            elif (tuple_value[0] == 'declaration'):
                self.handleDeclaration(tuple_value)
            else:
                for item in tuple_value:
                    if (type(item) == tuple):
                        self.iterate(item, whilePointer, endWhilePointer)


        except IndexError:
            print('Index out of range!')

    def handleAssignmentExpression(self, assignment):
        self
        global node, rightside
        leftside = assignment[1][1][1][1]
        variable = leftside
        rightside = assignment[3]
        if not self.checkNotExist(leftside):
            var = self.getVar(leftside)
            dtype = var['data-type']

            node = rightside[1]
            while node[0] != node[1][0]:
                if node[1][0] == 'primary-expression':
                    node = node[1]
                    break
                node = node[1]

            if node[0] == 'primary-expression':
                if node[1][0] == 'constant':
                    rightside = node[1][1]
                    if dtype == 'int' :
                        if not type(rightside) == int:
                            print('\033[91m semantic error: ', variable,' is ',dtype,' cant assign ',rightside, ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': rightside,
                                'address': self.memory
                            })
                            self.memory += 1
                    elif dtype == 'char':
                        if not type(rightside) == str:
                            print('\033[91m semantic error: ', variable, ' is ', dtype, ' cant assign ', rightside,
                                  ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': rightside,
                                'address': self.memory
                            })
                            self.memory += 1
                    elif dtype == 'float' or dtype == 'double':
                        if not type(rightside) == float:
                            print('\033[91m semantic error: ', variable, ' is ', dtype, ' cant assign ', rightside,
                                  ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': rightside,
                                'address': self.memory
                            })
                            self.memory += 1
                else:
                    rightside = node[1]
            else:
                self.handleAssignmentRightSide(node, variable, dtype)
                self.SymbolTable.append({
                    'variable': variable,
                    'data-type': dtype,
                    'value': None,
                    'address': self.memory
                })
                self.memory += 1
        else :
            print('\033[91m semantic error: ',leftside, ' not declare yet',
                  '\033[0m')


    def handleAssignmentRightSide(self, node,variable,dtype):
        global left, right
        if node[0] == 'logical-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][3])
        elif node[0] == 'logical-and-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'inclusive-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'exclusive-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'and-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'equality-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'relational-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'additive-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'multiplicative-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
        elif node[0] == 'cast-expression':
            print(node[1][1][0])
            return
        if left['isVar']:
            if not self.checkNotExist(left['value']):
                if right['isVar']:
                    if not self.checkNotExist(right['value']):
                        leftVar = self.getVar(left['value'])
                        rightVat = self.getVar(right['value'])
                        if not leftVar['data-type'] == rightVat['data-type']:
                            print('\033[91m semantic error: ', left['value'], ' and ',right['value']
                                  ,' dosent have same data type and cant do ',node[2],' operator ',
                                  '\033[0m')
                        else :
                            if not dtype == leftVar['data-type']:
                                print('\033[91m semantic error: ',' can not assign ',left['value'] ,node[2],right['value']
                                      , ' to ', variable,
                                      '\033[0m')

                    else :
                        print('\033[91m semantic error: ', right['value'], ' is not define and ', 'cant assign it to ',
                              variable,
                              '\033[0m')

                else :
                    leftVar = self.getVar(left['value'])
                    if type(right['value']) == int:
                        rigthDT = 'int'
                    elif type(right['value']) == float:
                        rigthDT = 'float'
                    elif type(right['value']) == str:
                        rigthDT = 'char'
                    if not rigthDT == leftVar['data-type']:
                        print('\033[91m semantic error: ', left['value'], ' and ', right['value']
                              , ' dosent have same data type and cant do ', node[2], ' operator ',
                              '\033[0m')

                    else :
                        if not dtype == leftVar['data-type']:
                            print('\033[91m semantic error: ', ' can not assign ', left['value'], node[2],
                                  right['value']
                                  , ' to ', variable,
                                  '\033[0m')
            else :
                print('\033[91m semantic error: ', left['value'], ' is not define and ', 'cant assign it to ', variable,
                      '\033[0m')

        else :
            if type(left['value']) == int:
                leftDT = 'int'
            elif type(left['value']) == float:
                leftDT = 'float'
            elif type(left['value']) == str:
                leftDT = 'char'

            if self.checkNotExist(left['value']):
                if right['isVar']:
                    if self.checkNotExist(right['value']):
                        rightVat = self.getVar(right['value'])
                        if not leftDT == rightVat['data-type']:
                            print('\033[91m semantic error: ', left['value'], ' and ', right['value']
                                  , ' dosent have same data type and cant do ', node[2], ' operator ',
                                  '\033[0m')
                        else:
                            if not dtype == leftDT:
                                print('\033[91m semantic error: ', ' can not assign ', left['value'], node[2],
                                      right['value']
                                      , ' to ', variable,
                                      '\033[0m')


                    else:
                        print('\033[91m semantic error: ', right['value'], ' is not define and ', 'cant assign it to ',
                              variable,
                              '\033[0m')

                else:
                    if type(right['value']) == int:
                        rigthDT = 'int'
                    elif type(right['value']) == float:
                        rigthDT = 'float'
                    elif type(right['value']) == str:
                        rigthDT = 'char'
                    if not rigthDT == leftDT:
                        print('\033[91m semantic error: ', left['value'], ' and ', right['value']
                              , ' dosent have same data type and cant do ', node[2], ' operator ',
                              '\033[0m')
                    else:
                        if not dtype == leftDT:
                            print('\033[91m semantic error: ', ' can not assign ', left['value'], node[2],
                                  right['value']
                                  , ' to ', variable,
                                  '\033[0m')
            else:
                print('\033[91m semantic error: ', left['value'], ' is not define and ', 'cant assign it to ', variable,
                      '\033[0m')
    def findExpLeftOrRightSide(self, node):

        while (node[1][0] != 'primary-expression'):
            node = node[1]
        node = node[1]
        if node[1][0] == 'constant':
            value =  node[1][1]
            return {
                'value':value,
                'isVar':False
            }
        else:
            value = node[1]
            return {
                'value': value,
                'isVar': True
            }

    def handleDeclaration(self, declaration):
        global node, dtype, value
        dtype = declaration[1][1][1]

        variable = declaration[3][1][1][1]

        node = declaration[3][1][3][1][1]

        if self.checkNotExist(variable):
            while node[0] != node[1][0]:
                if node[0] == 'primary-expression':
                    break
                node = node[1]

            if (node[0] == 'primary-expression'):
                if node[1][0] == 'constant':
                    value = node[1][1]
                    if dtype == 'int' :
                        if not type(value) == int:
                            print('\033[91m semantic error: ', variable,' is ',dtype,' cant assign ',value, ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': value,
                                'address': self.memory
                            })
                            self.memory += 1
                    elif dtype == 'char':
                        if not type(value) == str:
                            print('\033[91m semantic error: ', variable, ' is ', dtype, ' cant assign ', value,
                                  ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': value,
                                'address': self.memory
                            })
                            self.memory += 1
                    elif dtype == 'float' or dtype == 'double':
                        if not type(value) == float:
                            print('\033[91m semantic error: ', variable, ' is ', dtype, ' cant assign ', value,
                                  ' to variable', '\033[0m')
                        else :
                            self.SymbolTable.append({
                                'variable': variable,
                                'data-type': dtype,
                                'value': value,
                                'address': self.memory
                            })
                            self.memory += 1
                else:
                    value = node[1]
                    if self.checkNotExist(value):
                        value = self.getVar(value)
                        if dtype == value ['data-type']:
                            self.SymbolTable.append({
                                'variable' : variable,
                                'data-type' : dtype,
                                'value' : value['value'],
                                'address' : self.memory
                            })
                            self.memory += 1
                        else :
                            print('\033[91m semantic error: ', value, ' is ',value['data-type'], 'cant assign it to ',
                                  variable,' becuse its ',dtype, '\033[0m')
                    else :
                        print('\033[91m semantic error: ', value, ' is not define and ','cant assign it to ', variable, '\033[0m')

            else:
                self.handleAssignmentRightSide(node,variable,dtype)
                self.SymbolTable.append({
                    'variable': variable,
                    'data-type': dtype,
                    'value': None,
                    'address': self.memory
                })
                self.memory += 1

        else :
            print('\033[91m semantic error: ', variable , 'has already defind \033[0m')

    def getVar(self,var):
        for item in self.SymbolTable:
            if item['variable'] == var:
                return item

        return False
    def checkNotExist(self,var):
        for item in self.SymbolTable:
            if item['variable'] == var:
                return False

        return True




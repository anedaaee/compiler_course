import uuid

class CodeGeneration :
    def __init__(self,ast):
        self.ast = ast
        self.stack = {}
        self.memory = 0
        self.code = ''
        self.variableDef = ''
    def iterate(self,tuple_value,whilePointer='',endWhilePointer=''):
        try:

            if(tuple_value[0] == 'assignment-expression'):
                self.handleAssignmentExpression(tuple_value,whilePointer,endWhilePointer)
            elif(tuple_value[0] == 'declaration'):
                self.handleDeclaration(tuple_value,whilePointer,endWhilePointer)
            else:
                for item in tuple_value:
                    if(type(item) == tuple):
                        self.iterate(item,whilePointer,endWhilePointer)


        except IndexError:
            print('Index out of range!')

    def handleAssignmentExpression(self,assignment,whilePointer='',endWhilePointer=''):
        global node,rightside
        leftside = assignment[1][1][1][1]
        rightside = assignment[3]

        node = rightside[1]
        while node[0] != node[1][0]:
            if node[1][0] == 'primary-expression':
                node = node[1]
                break
            node = node[1]

        if node[0] == 'primary-expression':
            if node[1][0] == 'constant':
                rightside = node[1][1]
            else :
                rightside = node[1]
            self.code += '\t'+'MOV ' +str(leftside) + ' ' + str(rightside) + '\n'
        else:
            self.handleAssignmentRightSide(node)
            self.code += '\t'+'MOV '+str(leftside)+' EAX'+ '\n'

    def handleAssignmentRightSide(self,node):

        global left,right
        if node[0] == 'logical-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][3])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'OR EAX '+ str(left) + '\n'
        elif node[0] == 'logical-and-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'AND EAX '+ str(left) + '\n'
        elif node[0] == 'inclusive-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'OR EAX '+ str(left) + '\n'
        elif node[0] == 'exclusive-or-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'XOR EAX '+ str(left) + '\n'
        elif node[0] == 'and-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'AND EAX '+ str(left) + '\n'
        elif node[0] == 'equality-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'CMP EAX '+ str(left) + '\n'
            self.code += '\t'+'CMP EAX ZF\n'
        elif node[0] == 'relational-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            self.code += '\t'+'CMP EAX '+ str(left) + '\n'
            self.code += '\t'+'MOV EAX SF'+'\n'
        elif node[0] == 'additive-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            if node[2] == '+':
                self.code += '\t'+'ADD '+ str(left)+' EAX' + '\n'
            elif node[2] == '-':
                self.code += '\t'+'SUB '+ str(left) +' EAX'+ '\n'
            self.code += '\t'+'MOV EAX ' + str(left)  + '\n'
        elif node[0] == 'multiplicative-expression':
            left = self.findExpLeftOrRightSide(node[1][1])
            right = self.findExpLeftOrRightSide(node[3][1])
            self.code += '\t'+'MOV EAX ' + str(right) + '\n'
            if node[2] == '*':
                self.code += '\t'+'MUL ' + str(left) +' EAX'+ '\n'
            elif node[2] == '/':
                self.code -= '\t'+'DIV ' + str(left) +' EAX'+ '\n'
            self.code += '\t'+'MOV EAX ' + str(left) + '\n'


    def findExpLeftOrRightSide(self,node):

        while(node[1][0] != 'primary-expression'):
            node = node[1]
        node = node[1]
        if node[1][0] == 'constant':
            return node[1][1]
        else :
            return node[1]


    def handleDeclaration(self,declaration,whilePointer='',endWhilePointer=''):
        global node , dtype , value
        dtype = declaration[1][1][1]
        if dtype == 'float' :
            dtype = 'SINGLE,S'
        elif dtype == 'double':
            dtype = 'DOUBLE,D'
        elif dtype == 'char':
            dtype = 'CHAR,DB'
        else :
            dtype = 'DD'
        variable = declaration[3][1][1][1]

        node = declaration[3][1][3][1][1]

        while node[0] != node[1][0]:
            if node[0] == 'primary-expression':
                break
            node = node[1]
        self.variableDef += variable + ' : ' + dtype + '0\n'
        if(node[0] == 'primary-expression'):
            if node[1][0] == 'constant':
                value = node[1][1]
            else :
                value = node[1]
            self.code += '\t'+'MOV ' + str(variable) + ' ' + str(value) + '\n'
        else :
            self.handleAssignmentRightSide(node)
            self.code += '\t'+'MOV ' + str(variable) + ' EAX' + '\n'

        self.stack[variable] = self.memory
        self.memory += 1


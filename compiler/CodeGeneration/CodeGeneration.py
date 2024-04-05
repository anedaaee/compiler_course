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

            if tuple_value[0] == 'iteration-statement':
                self.handleiterationStatement(tuple_value,whilePointer,endWhilePointer)
            elif(tuple_value[0] == 'selection-statement'):
                self.handleSelectionStatement(tuple_value,whilePointer,endWhilePointer)
            elif tuple_value[0] == 'jump-statement':
                self.handleJumpStatement(tuple_value,whilePointer,endWhilePointer)
            elif(tuple_value[0] == 'assignment-expression'):
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

    def handleSelectionStatement(self,ifElse,whilePointer='',endWhilePointer=''):

        global ifPointer,elsePointer,condition,leftSide,rightSide
        if (ifElse[1]):
            ifPointer = 'IF '+ str(uuid.uuid4())
        if (ifElse[6]):
            elsePointer = 'ELSE ' + str(uuid.uuid4())

        condition = ifElse[3]

        while condition[0] != condition[1][0]:
            if condition[1][0] == 'primary-expression':
                condition = condition[1]
                break
            condition = condition[1]
        operator = condition[0]
        leftSide = condition[1]
        rightSide = condition[3]
        while leftSide[0] != 'primary-expression':
            leftSide = leftSide[1]
        while rightSide[0] != 'primary-expression':
            rightSide = rightSide[1]

        if leftSide[0] == 'primary-expression':
            if leftSide[1][0] == 'constant':
                leftSide = leftSide[1][1]
            else :
                leftSide = leftSide[1]

        if rightSide[0] == 'primary-expression':
            if rightSide[1][0] == 'constant':
                rightSide = rightSide[1][1]
            else :
                rightSide = rightSide[1]

        self.code += '\t'+'MOV EAX ' + str(leftSide) +'\n'
        self.code += '\t'+'MOV EBX ' + str(rightSide) +'\n'
        self.code += '\t'+'CMP EAX EBX' + '\n'

        if operator == '\t'+'equality-expression':
            if condition[2] == '==':
                self.code += '\t'+'JE '+ ifPointer + '\n'
                self.code += '\t'+'JNE '+ elsePointer + '\n'
            elif condition[2] == '!=':
                self.code += '\t'+'JE '+ elsePointer + '\n'
                self.code += '\t'+'JNE '+ ifPointer + '\n'

        elif operator == 'relational-expression':
            if condition[2] == '>':
                self.code += '\t'+'JG '+ ifPointer + '\n'
                self.code += '\t'+'JLE '+ elsePointer + '\n'
            elif condition[2] == '>=':
                self.code += '\t'+'JGE '+ ifPointer + '\n'
                self.code += '\t'+'JL '+ elsePointer + '\n'
            elif condition[2] == '<':
                self.code += '\t'+'JL '+ ifPointer + '\n'
                self.code += '\t'+'JGE '+ elsePointer + '\n'
            elif condition[2] == '<=':
                self.code += '\t'+'JLE '+ ifPointer + '\n'
                self.code += '\t'+'JG '+ elsePointer + '\n'

        self.code += str(ifPointer) + ': \n'
        self.iterate(ifElse[5],whilePointer,endWhilePointer)
        self.code += str(elsePointer) + ': \n'
        self.iterate(ifElse[7],whilePointer,endWhilePointer)

    def handleiterationStatement(self,whileState,whilePointer='',endWhilePointer=''):
        global condition,leftSide,rightSide

        if whileState[1]:
            whilePointer = 'WHILE ' + str(uuid.uuid4())
            endWhilePointer = 'END WHILE ' + str(uuid.uuid4())

        self.code += str(whilePointer) + ': \n'
        self.iterate(whileState[5],whilePointer,endWhilePointer)

        condition = whileState[3]
        print(condition)
        while condition[0] != condition[1][0]:
            if condition[1][0] == 'primary-expression':
                condition = condition[1]
                break

            condition = condition[1]

        operator = condition[0]
        leftSide = condition[1]
        rightSide = condition[3]
        while leftSide[0] != 'primary-expression':
            leftSide = leftSide[1]
        while rightSide[0] != 'primary-expression':
            rightSide = rightSide[1]

        if leftSide[0] == 'primary-expression':
            if leftSide[1][0] == 'constant':
                leftSide = leftSide[1][1]
            else :
                leftSide = leftSide[1]

        if rightSide[0] == 'primary-expression':
            if rightSide[1][0] == 'constant':
                rightSide = rightSide[1][1]
            else :
                rightSide = rightSide[1]

        self.code += '\t'+'MOV EAX ' + str(leftSide) +'\n'
        self.code += '\t'+'MOV EBX ' + str(rightSide) +'\n'
        self.code += '\t'+'CMP EAX EBX' + '\n'

        if operator == '\t'+'equality-expression':
            if condition[2] == '==':
                self.code += '\t'+'JE '+ whilePointer + '\n'
                self.code += '\t'+'JNE '+ endWhilePointer + '\n'
            elif condition[2] == '!=':
                self.code += '\t'+'JE '+ endWhilePointer + '\n'
                self.code += '\t'+'JNE '+ whilePointer + '\n'

        elif operator == 'relational-expression':
            if condition[2] == '>':
                self.code += '\t'+'JG '+ whilePointer + '\n'
                self.code += '\t'+'JLE '+ endWhilePointer + '\n'
            elif condition[2] == '>=':
                self.code += '\t'+'JGE '+ whilePointer + '\n'
                self.code += '\t'+'JL '+ endWhilePointer + '\n'
            elif condition[2] == '<':
                self.code += '\t'+'JL '+ whilePointer + '\n'
                self.code += '\t'+'JGE '+ endWhilePointer + '\n'
            elif condition[2] == '<=':
                self.code += '\t'+'JLE '+ whilePointer + '\n'
                self.code += '\t'+'JG '+ endWhilePointer + '\n'

        self.code += str(endWhilePointer) + ': \n'



    def handleJumpStatement(self,jump,whilePointer,endWhilePointer):

        if jump[1] == 'break' :
            self.code += '\t' + 'JMP '+ endWhilePointer + '\n'
        elif jump[1] == 'continue' :
            self.code += '\t' + 'JMP '+ whilePointer + '\n'

    def writeResult(self):
        file = open('code.txt', 'w')
        file.write(self.variableDef)
        file.write(self.code)
        file.close()
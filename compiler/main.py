import ply.lex as lex
import ply.yacc as parser

from Lexer.lexer import *
from Parser.parser3 import *
from Semantic.Semantic import Semantic
from CodeGeneration.CodeGeneration2 import  CodeGeneration
lexer = lex.lex()


with open('programs/program1.c', 'r') as file:
    program = file.read()

lexer.input(program)

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok)

parser = parser.yacc(debug=True,start='translation-unit',method='SLR')

ast = parser.parse(program)

print(ast)

CG  = CodeGeneration(ast)
CG.iterate(CG.ast)
print(CG.variableDef)
print(CG.code)
print(CG.stack)

semantic = Semantic(ast)

semantic.iterate(semantic.ast)
print(semantic.SymbolTable)
CG.writeResult()


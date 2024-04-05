import lexer

tokens = []

lx = lexer.Lexer('../programs/program1.txt','../csv/compilerDFATable - Sheet1.csv')

lx.readDataFromCsv()
lx.readProgram()

while(lx.hasNext()):
    token = lx.getNextToken()
    if(token is not None):
        tokens.append(token)

for token in tokens:
    print(token)

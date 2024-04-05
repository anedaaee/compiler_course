import pandas as pd
import numpy as np


class Lexer :
    def __init__(self , program_path , csv_path):
        #file paths
        self.program_path = program_path
        self.csv_path = csv_path
        # our line and character counter
        self.line_count = 1
        self.char_count = 1
        self.char_in_line_count = 1
        # our token counter
        self.token_count = 0
        # finite states
        self.states = {
            "0" : "start",
            "12" : "keyword",
            "14" : "identifier",
            "17" : "number",
            "18" : "operators",
            "19" : "punctuators",
            "20" : "dom"
        }


    def readDataFromCsv(self):
        #read data as pandas dataframe
        csv_data = pd.read_csv(self.csv_path)
        #extract alphabet of language from csv dataframe
        self.alpha = csv_data.columns.to_numpy()
        self.alpha = np.delete(self.alpha,0)
        # these lines change \\t to \t and \\n to \n and \\v to \v and \\f to \f and \\r to \r
        self.alpha[67] = '\t'
        self.alpha[68] = '\n'
        self.alpha[69] = '\v'
        self.alpha[70] = '\f'
        self.alpha[71] = '\r'
        #extract DFA datatable from csv dataframe
        self.dfa_data = np.array(csv_data)

        self.dfa_data  = self.dfa_data[:,1:]

    def readProgram(self):
        #read program file
        with open(self.program_path,'r') as file :
            file_content = file.read()
        #set program string to input program file
        self.program_string = file_content

    #this function get dfa column
    def getColumn(self,ch):
        return np.where(self.alpha == ch)[0]
    #this function return true if our program has not finished
    def hasNext(self):
        index = self.char_count - 1
        program = self.program_string[index:]
        if(program == ""):
            return False
        return True
    def getNextToken(self):
        # these two line find current charat of program
        index = self.char_count - 1
        program = self.program_string[index:]
        # these two line get start line and char index of new lexem
        start_line = self.line_count
        start_ch = self.char_in_line_count
        # initialize current state with 0 (start state)
        current_state = 0
        # lexem string is a lexem that this function will find
        lexem = ""
        # this loop will see characters and recognize lexem
        for i,ch in enumerate(program):
            # concat lexem with character
            lexem += ch
            # update current state with next state
            current_state = self.dfa_data[current_state][self.getColumn(ch)]
            current_state = current_state[0]
            # add 1 to out character counters
            self.char_in_line_count += 1
            self.char_count += 1
            # if current state is finite state
            if self.states.get(str(current_state)) is not None:
                # if we are not in start state
                if(self.states.get(str(current_state)) != 'start'):
                    # if current state is dom or error
                    if(self.states.get(str(current_state)) == 'dom'):
                        # these lines find next state to make sure we finish error lexem
                        if i < len(program) -1 :
                            next_ch = program[i+1]
                            next_state = self.dfa_data[current_state][self.getColumn(next_ch)]
                            next_state = next_state[0]
                        # if next state is not dom or error that shows we finish error lexem
                        if(self.states.get(str(next_state)) != 'dom'):
                            # because we found lexem we increase the token counter
                            self.token_count += 1

                            # create error token object or dict that we will return
                            token = {
                                "ID" : str(self.token_count),
                                "Type" : "ERROR",
                                "Line" : str(start_line)+"["+str(start_ch)+"]",
                                "Lexem" : lexem
                            }
                            if (ch == '\n'):
                                self.line_count += 1
                                self.char_in_line_count = 1
                                start_line = self.line_count
                                start_ch = self.char_in_line_count
                            return token
                    else:
                        # because we found lexem we increase the token counter
                        self.token_count += 1

                        # create not error token (operator , number , ...) object or dict that we will return

                        token = {
                            "ID": str(self.token_count),
                            "Type": self.states.get(str(current_state)),
                            "Line": str(start_line) + "[" + str(start_ch) + "]",
                            "Lexem": lexem
                        }
                        if (ch == '\n'):
                            self.line_count += 1
                            self.char_in_line_count = 1
                            start_line = self.line_count
                            start_ch = self.char_in_line_count
                        return token
                else :
                    #if next state is start we will clear lexem
                    lexem= ""

            if (ch == '\n'):
                self.line_count += 1
                self.char_in_line_count = 1
                start_line = self.line_count
                start_ch = self.char_in_line_count
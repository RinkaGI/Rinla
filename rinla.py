############ CONSTANTS ####################
DIGITS = '0123456789'
TUTORIAL = 'https://www.youtube.com/watch?v=Eythq9848Fg&t=6shttps://www.youtube.com/watch?v=Eythq9848Fg&t=6s'

############ TOKENS ######################
TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

################## ERROR MSG ##################
# TODO: make a class for make errors msg and detects illegal chars

################# LEXER ####################

# lexer is for detects each symbol in code
# lexer works with detecting pos and the current_char
# goes on the code, detects each symbol and if it is a recognised symbol, save it. If its a number, make a special work
# special work is advancing until stops the recongising (maybe number, or if its a more than 1 char of token, detects that is all equal)

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()


    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None

    def makeNumbers(self):
        numstr = ''
        dotCount = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dotCount == 1: break
                dotCount += 1
                numstr += '.'
            else:
                numstr += self.current_char

        if dotCount == 0:
            return Token(TT_INT, int(numstr))
        else:
            return Token(TT_FLOAT, float(numstr))

    def makeTokens(self):
        tokens = []

        while self.current_char != None:
            # Ignoring spaces
            if self.current_char in ' \t':
                self.advance()
            
            # Detect simple operator symbols
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()

            #detect parens
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))

            #detect digits
            elif self.current_char in DIGITS:
                tokens.append(makeNumbers())

            else:
                print('No detected!')
            

        return tokens

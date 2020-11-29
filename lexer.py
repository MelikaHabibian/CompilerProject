DIGITS      = '0123456789'


class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name} : {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result


class IllegalCharacterError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)




t_INT       = 'Sahih'
t_FLOAT     = 'Ashari'
t_PLUSONE   = 'YekiBala'
t_PLUS      = 'Jam'
t_MINUSONE  = 'YekiPain'
t_MINUS     = 'Kam'
t_TIMES     = 'Zarb'
t_DIVIDE    = 'Tagsim'
t_EQ        = '&MM'
t_LT        = '&K'
t_GT        = '&B'
t_LTE       = '&KM'
t_GTE       = '&BM'
t_REMAINED  = 'Bagimonde'
t_LPAREN   = 'LParent'
t_RPAREN   = 'RParent'
t_LBrow    =  'Lbrow'
t_RBrow    =  'Rbrow'




class Token:


    def __init__(self, type_, value=None):
      self.type  = type_
      self.value = value

    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
      self.pos.advance(self.current_char)
      self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def makeTokens(self):
        tokens  = []


        while self.current_char != None:
            if self.current_char in '\t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '++':
                 tokens.appened(Token(t_PLUSONE))
                 self.advance()
            elif self.current_char == '+':
                 tokens.append(Token(t_PLUS))
                 self.advance()
            elif self.current_char == '--':
                 tokens.appened(Token(t_MINUSONE))
                 self.advance()
            elif self.current_char == '-':
                 tokens.appened(Token(t_MINUS)) 
                 self.advance()   
            elif self.current_char == '*':
                 tokens.appened(Token(t_TIMES))
                 self.advance()
            elif self.current_char == '/':
                 tokens.appened(Token(t_DIVIDE))
                 self.advance()

            elif self.current_char == '{':
                tokens.append(Token(t_LBrow))
                self.advance()
            elif self.current_char == '}':
                tokens.append(Token(t_RBrow))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(t_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(t_RPAREN))
                self.advance()    
            else:
                pos.start = self.pos.copy
                char      = self.current_char
                self.advance()
                return[], IllegalCharacterError(pos_start, self.pos,  "'" + char +"'")
        return tokens, None
            
    def make_number(self):
        num_str   = ''
        dot_count = 0

        while self.current_char != None and self.current.char in DIGITS + '.':
            if self.current_char == '.':
               if dot_count      == 1: break
               dot_count += 1
               num_str    ='.'
            else:
                num_str += self.current_char
                self.advance()

        if dot_count == 0:
            return Token(t_INT, int(num_str))
        else:
            return Token(t_FLOAT, float(num_str))



def run( fn, text):
    lexer =  Lexer(fn, text)
    tokens, error = lexer.makeTokens()

    return tokens, error












import re
import readline
from data_types import *

class Reader:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def next(self):
        result = self.tokens[self.pos]
        self.pos += 1
        return result


def read_str(string):

    tokens = tokenizer(string)
    reader = Reader(tokens)

    result = read_form(reader)
    
    return result

def tokenizer(string):

    pcre = r'''[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)'''
    result = re.findall(pcre, string)

    return result

def read_form(reader):

    first_token = reader.peek()
    if first_token == '(':
        result = read_list(reader)
    else:
        result = read_atom(reader)
    return result

def read_list(reader):
    result = []

    # throw first "(" away
    reader.next()
    
    while reader.peek() != ')':
        token = read_form(reader)
        # TODO: handle EOF gracefully
        #if token == '':
        #    raise EOFError(f"last token {token}")
        result.append(token)
    
    # throw last ")" away
    reader.next()
    
    return result

def read_atom(reader):

    content = reader.next()
    
    if content == 'nil':
        return Nil()

    elif content in ['true', 'false']:
        return Bool(content)
        
    elif content.isnumeric() or (
        (len(content) >= 2) and 
        content[0] == '-' and 
        content[1:].isnumeric()):
        return Integer(content)

    elif content.startswith('"') and content.endswith('"'):
        s = content[1:-1]
        chars = []
        skip = False
        for a, b in zip(s[:-1], s[1:]):
            if skip:
                skip = False
                continue
            if a == '\\':
                if b == 'n':
                    chars.append('\n')
                    skip = True
                elif b == '\\':
                    chars.append('\\')
                    skip = True
                elif b == '"':
                    chars.append('"')
                    skip = True
            else:
                chars.append(a)
        if s and not skip:
            chars.append(s[-1])
        return String(''.join(chars))
    else:
        return Symbol(content)



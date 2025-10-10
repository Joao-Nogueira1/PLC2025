import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<S>SELECT|select)|(?P<W>WHERE|where)|(?P<LIM>LIMIT|limit)|(?P<INT>\d+)|(?P<VAR>\?\w+)|(?P<ABREV>a)|(?P<ID>\w*:\w+)|(?P<LSTRING>"(\w+ ?)+")|(?P<LTAG>@\w+)|(?P<PONTO>\.)|(?P<PA>\{)|(?P<PF>\})|(?P<SKIP>( )|(\t)|(#.*\n))|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['S']:
            t = ("S", dic['S'], linha, m.span())

        elif dic['W']:
            t = ("W", dic['W'], linha, m.span())
    
        elif dic['LIM']:
            t = ("LIM", dic['LIM'], linha, m.span())
    
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['ABREV']:
            t = ("ABREV", dic['ABREV'], linha, m.span())
    
        elif dic['ID']:
            t = ("ID", dic['ID'], linha, m.span())
    
        elif dic['LSTRING']:
            t = ("LSTRING", dic['LSTRING'], linha, m.span())
    
        elif dic['LTAG']:
            t = ("LTAG", dic['LTAG'], linha, m.span())
    
        elif dic['PONTO']:
            t = ("PONTO", dic['PONTO'], linha, m.span())
    
        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())
    
        elif dic['PF']:
            t = ("PF", dic['PF'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)

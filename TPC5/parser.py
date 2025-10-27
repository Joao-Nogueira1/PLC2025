from analex import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)


# p1: Exp → T ExpL
# p2: ExpL → Op T
# p3:      | eps  
# p4: T → F ExpL
# p5: F → num 
# p6:   | '(' Exp ')'



# p2: ExpL → Op EXPLL
#     ExpL -> eps  
#     EXPLL -> F ExpL
#     EXPLL -> T ExpL

def rec_F():
    global prox_simb
    print(prox_simb)
    if prox_simb.type == 'NUM':
        print("Derivando por P5: F    --> num")
        rec_term('NUM')
        print("Reconheci P5: F    --> num")
    elif prox_simb.type == 'PA':
        print("Derivando por P6: F --> '(' Exp ')'")
        rec_term('PA')
        rec_Exp()
        rec_term('PF')
        print("Reconheci P6: Cont2 --> '(' Exp ')'")
    else:
        parserError(prox_simb)

# p4: T → F ExpL

def rec_T():
    global prox_simb
    print("Derivando por P4: T -> F ExpL")
    rec_F()
    rec_ExpL()
    print("Reconheci P4: T -> F ExpL")

# p2: ExpL → Op T
# p3:      | eps  

def rec_ExpL():
    global prox_simb
    if (prox_simb!=None) and prox_simb.type == 'OP':
        print("Derivando por P2: ExpL --> Op T")
        rec_term('OP')
        rec_T()
        print("Reconheci P2: ExpL --> Op T")
    elif (prox_simb==None) or (prox_simb.type == 'PF' or prox_simb.type == 'NUM'):
        print("Derivando por P3: Expl-->")
        print("Reconheci P3: Expl -->")
    else:
        parserError(prox_simb)

# p1: Exp → T ExpL

def rec_Exp():
    global prox_simb
    print("Derivando por P1: Exp --> T ExpL")
    rec_T()
    rec_ExpL()
    print("Reconheci P1: Exp --> T ExpL")

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    rec_Exp()
    print("That's all folks!")


linha = input("Introduza uma expressao: ")
rec_Parser(linha)
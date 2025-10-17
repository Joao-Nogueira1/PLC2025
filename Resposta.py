import re 
import ply.lex as lex
import json
import datetime as datetime

def verificar_data():
    data = datetime.datetime.now().strftime("%Y-%m-%d")
    padrao = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    if  padrao.match(data):
        return data
    else:
        print("Data não aceite")

with open("stock.json", "r", encoding="utf-8") as f:
    stock = json.load(f)

print(f"{verificar_data()}. Stock carregado, Estado atualizado.")
print("Bom dia. Estou disponível para atender o seu pedido.")

budget=0

def saldo(escrita_moedas):
    global budget
    if escrita_moedas.startswith("MOEDA"):
        dinheiro = escrita_moedas[6:].strip()
        verifica_saldo = re.compile(r"^(\d+[ec])*(,\s*\d+[c])*\.?$")
        if verifica_saldo.fullmatch(dinheiro):
            euros_lista=re.findall(r'(\d+)e', dinheiro)
            centimos_lista = re.findall(r'(\d+)c', dinheiro)
            euros=sum(int(c) for c in euros_lista)
            centimos=sum(int(c) for c in centimos_lista)
            budget+=euros*100+centimos
            print(f'maq: Saldo = {budget//100}e {budget%100}c')


def selecao(escrita_selecao):
    global budget
    for elemento in stock["stock"]:
        if escrita_selecao.split()[1] == elemento["cod"]:
            if budget>=elemento["preco"]*100:
                budget=budget-elemento["preco"]*100
                elemento["quant"]-=1
                print(f"maq: Pode retirar o produto dispensado {elemento['nome']}")
                print(f"maq: Saldo = {budget//100}e {budget%100}c")
            else: 
                print("Saldo insuficiente para satisfazer o seu pedido")
                preco_copia=elemento["preco"]*100
                print(f"maq: Saldo: {budget//100}e {budget%100}c; Pedido:{preco_copia//100}e {preco_copia%100}")




while True:
    interacao=input(">>")
    if interacao.startswith("LISTAR"):
        print("cod    |  nome      |  quantidade  |  preço ")
        print("---------------------------------")
        for item in stock["stock"]:
            print(f"{item['cod']:<6} | {item['nome']:<10} | {item['quant']:<12} | {item['preco']:<6.2f}")
    if interacao.startswith("MOEDA"):
        saldo(interacao)
    if interacao.startswith("SELECIONAR"):
        selecao(interacao)
    if interacao.startswith("SAIR"):
        moeda2=0
        moeda1=0
        moeda50=0
        moeda20=0
        moeda10=0
        moeda5=0
        moeda2c=0
        moeda1c=0

        while budget>0:
            if budget>=200:
                moeda2+=1
                budget-=200
            elif budget>=100:
                moeda1+=1
                budget-=100
            elif budget>=50:
                moeda50+=1
                budget-=50
            elif budget>=20:
                moeda20+=1
                budget-=20
            elif budget>=10:
                moeda10+=1
                budget-=10
            elif budget>=5:
                moeda5+=1
                budget-=5
            elif budget>=2:
                moeda2c+=1
                budget-=2
            elif budget>=1:
                moeda1c+=1
                budget-=1


        partes = []
        if moeda2: partes.append(f"{moeda2}x 2e")
        if moeda1: partes.append(f"{moeda1}x 1e")
        if moeda50: partes.append(f"{moeda50}x 50c")
        if moeda20: partes.append(f"{moeda20}x 20c")
        if moeda10: partes.append(f"{moeda10}x 10c")
        if moeda5:  partes.append(f"{moeda5}x 5c")
        if moeda2c:  partes.append(f"{moeda2c}x 2c")
        if moeda1c:  partes.append(f"{moeda1c}x 1c")

        if partes:
                print("Pode retirar o troco: " + ", ".join(partes))
                print("Até à próxima")
        else:
                print("Sem troco a devolver.")
                print("Até à próxima")


        break




with open('stock.json', 'w', encoding='utf-8') as f:
    json.dump(stock, f, indent=4)

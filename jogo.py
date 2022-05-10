
import random
from math import *
import funcoes
import dados

vidas=20

print('\n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \nComandos:\ndica       - entra no mercado de dicas\ndesisto    - desiste da rodada\ninventario - exibe sua posição')

paises=funcoes.normaliza(dados.DADOS)

resposta=funcoes.sorteia_pais(paises)
print('O pais foi escolhido!')

term=''

while vidas>0:
    print('Você tem', vidas,'tentativas \nQual o seu palpite?' )
    tentativa=input()
    while tentativa not in paises.keys():
        print('pais desconhecido')
        print('Você tem', vidas,'\nQual o seu palpite?')
        tentativa=input()

    if tentativa != resposta:
        vidas-=1
        term+=tentativa
        term+='\n'
        term+= str(int(funcoes.haversine(6371,paises[tentativa]['geo']['latitude'],paises[resposta]['geo']['longitude'],paises[resposta]['geo']['latitude'],paises[tentativa]['geo']['longitude'])))
        print(term)


import random
from math import *
import funcoes
import dados



print('\n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \nComandos:\ndica       - entra no mercado de dicas\ndesisto    - desiste da rodada\ninventario - exibe sua posição')

paises=funcoes.normaliza(dados.DADOS)
jogarnovamente='s'

while jogarnovamente=='s':

    resposta=funcoes.sorteia_pais(paises)
    print('O pais foi escolhido!\n')
    vidas=20
    paisesordenados=[]

    while vidas>0:
        print('\nVocê tem', vidas,'tentativas' )
        tentativa=input( '\nQual o seu palpite? ')

        while tentativa not in paises.keys():
            print('pais desconhecido')
            print('\nVocê tem', vidas,'')
            tentativa=input('\nQual o seu palpite? ')

        if tentativa != resposta:
            vidas-=1            
            dist= (int(funcoes.haversine(6371,paises[tentativa]['geo']['latitude'],paises[resposta]['geo']['longitude'],paises[resposta]['geo']['latitude'],paises[tentativa]['geo']['longitude'])))
            paisesordenados = funcoes.adiciona_em_ordem(tentativa,dist,paisesordenados)
            print('\nDistâncias:\n')
            for i in range(len(paisesordenados)):
                print(paisesordenados[i][1],'km ->',paisesordenados[i][0])
        
        if tentativa == resposta:
            print('*** Parabéns! Você acertou após 7 tentativas!\n\nJogar novamente? [s|n]')


    if vidas<=0:
        print('>>> Você perdeu, o país era: ', resposta)
        print('\n\nJogar novamente? [s|n]')


    jogarnovamente=input('Jogar novamente? [s|n] ')

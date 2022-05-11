
import random
from math import *
import funcoes
import dados



print('\n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \nComandos:\ndica       - entra no mercado de dicas\ndesisto    - desiste da rodada\ninventario - exibe sua posição')

paises=funcoes.normaliza(dados.DADOS)
jogarnovamente='s'

while jogarnovamente=='s':

    resposta=funcoes.sorteia_pais(paises)
    print('Um pais foi escolhido, tente adivinhar!\n')
    vidas=20
    paisesordenados=[]

    while vidas>0:
        print('\nVocê tem', vidas,'tentativas' )
        tentativa=input( '\nQual o seu palpite? ')

        while tentativa not in paises.keys() and tentativa != 'desisto':
            print('pais desconhecido')
            print('\nVocê tem', vidas,'')
            tentativa=input('\nQual o seu palpite? ')

        if tentativa != resposta and funcoes.esta_na_lista(tentativa,paisesordenados)==False and tentativa != 'desisto':
            vidas-=1            
            dist= (int(funcoes.haversine(6371,paises[tentativa]['geo']['latitude'],paises[tentativa]['geo']['longitude'],paises[resposta]['geo']['latitude'],paises[resposta]['geo']['longitude'])))
            paisesordenados = funcoes.adiciona_em_ordem(tentativa,dist,paisesordenados)
            print('\nDistâncias:')
            for i in range(len(paisesordenados)):
                print('    ', paisesordenados[i][1],'km ->',paisesordenados[i][0])
        
        if tentativa == resposta:
            print('\n*** Parabéns! Você acertou após', 21-vidas ,'tentativas!')
            jogarnovamente=input('\nJogar novamente? [s|n] ')
            break

        if tentativa == 'desisto':
            desistir = str(input('Tem certeza que deseja desistir da rodada? [s|n]'))
            if desistir == 's':
                print('>>> Que deselegante desistir, o país era:', resposta)
                jogarnovamente=input('\nJogar novamente? [s|n] ')
                break
            


    if vidas<=0:
        print('>>> Você perdeu, o país era: ', resposta)
        jogarnovamente=input('\nJogar novamente? [s|n] ')



print('\n\n\nAté a próxima!')
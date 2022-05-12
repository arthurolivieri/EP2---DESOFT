
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
    dicasdadas = []

    while vidas>0:
        print('\nVocê tem', vidas,'tentativas' )
        tentativa=input( '\nQual o seu palpite? ')

        while tentativa not in paises.keys() and tentativa != 'desisto' and tentativa != 'dica':
            print('pais desconhecido')
            print('\nVocê tem', vidas,'')
            tentativa=input('\nQual o seu palpite? ')

        if tentativa != resposta and funcoes.esta_na_lista(tentativa,paisesordenados)==False and tentativa != 'desisto' and tentativa != 'dica':
            vidas-=1            
            dist= (int(funcoes.haversine(6371,paises[tentativa]['geo']['latitude'],paises[tentativa]['geo']['longitude'],paises[resposta]['geo']['latitude'],paises[resposta]['geo']['longitude'])))
            paisesordenados = funcoes.adiciona_em_ordem(tentativa,dist,paisesordenados)
            print('\nDistâncias:')
            for i in range(len(paisesordenados)):
                print('    ', paisesordenados[i][1],'km ->',paisesordenados[i][0])
            print('\nDicas:')
            for d in dicasdadas:
                print ('    ', d)
        
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

        if tentativa == 'dica':
            print('\nMercado de Dicas\n----------------------------------------\n1. Cor da bandeira  - custa 4 tentativas\n2. Letra da capital - custa 3 tentativas\n3. Área             - custa 6 tentativas\n4. População        - custa 5 tentativas\n5. Continente       - custa 7 tentativas\n0. Sem dica\n----------------------------------------')
            dica = int(input('Escolha sua opção [0 | 1 | 2 | 3 | 4 | 5]:'))
            if dica == 1:
                dicasdadas.append('  - Cores da bandeira') #adicionar cor
                vidas -= 4
            if dica == 2:
                dicasdadas.append('  - Letras da capital: ', funcoes.sorteia_letra(paises[resposta]['capital'], ['-']))
                vidas -= 3
            if dica == 3:
                dicasdadas.append('  - Área: ', paises[resposta]['area'])
                vidas -= 6
            if dica == 4:
                dicasdadas.append('  - População: ', paises[resposta]['populacao'], 'pessoas')
                vidas -= 5
            if dica == 5:
                dicasdadas.append('  - Continente: ', paises[resposta]['continente'])
                vidas -= 7


    if vidas<=0:
        print('>>> Você perdeu, o país era: ', resposta)
        jogarnovamente=input('\nJogar novamente? [s|n] ')



print('\n\n\nAté a próxima!')
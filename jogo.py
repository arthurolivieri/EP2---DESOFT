
import random
from math import *
import funcoes
import dados


print('\n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \nComandos:\ndica       - entra no mercado de dicas\ndesisto    - desiste da rodada\ninventario - exibe sua posição')

paises=funcoes.normaliza(dados.DADOS)

mercadodedicas=['Mercado de Dicas\n',
'----------------------------------------\n',
'1. Cor da bandeira  - custa 4 tentativas\n',
'2. Letra da capital - custa 3 tentativas\n',
'3. Área             - custa 6 tentativas\n',
'4. População        - custa 5 tentativas\n',
'5. Continente       - custa 7 tentativas\n',
'0. Sem dica\n',
'----------------------------------------\n']

jogarnovamente='s'

while jogarnovamente=='s':

    resposta=funcoes.sorteia_pais(paises)
    print('Um pais foi escolhido, tente adivinhar!\n')
    cores=[]

    #adiciona as cores em uma lista
    for chave,valor in paises[resposta]['bandeira'].items():
        if valor>0 :
            cores.append(chave)
    if 'outras' in cores:
        cores.remove('outras')
    
    restrito=[] #cria uma lista de palavras restritas para a dica da capital

    vidas=20 #variavel que conta a quantidade de vidas/tentativas restantes

    paisesordenados=[]

    dicasdadas = []

    dica='0' #variavel que guarda a dica usada (começa em '0' para entrar no loop)

    opcoes=['1','2','3','4','5','0'] #lista de opcoes de dicas

    while vidas>0: #loop para caso de derrota

        if dica not in opcoes:
            tentativa='dica'
        
        else:
            if dicasdadas:
                for i in range(len(dicasdadas)):
                    print (dicasdadas[i][0],dicasdadas[i][1])
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
            if dica not in opcoes:
                dica = input()
            else:
                for i in mercadodedicas:
                    print(i)
                print('Escolha sua opção [0 | 1 | 2 | 3 | 4 | 5]: ')
                dica = input()
            if dica not in opcoes:
                print('Opção inválida')
                continue
            elif int(dica) == 1:
                cordica=cores[random.randint(0,len(cores)-1)]
                dicasdadas.append(['  - Cor da bandeira: ', cordica])
                cores.remove(cordica)
                vidas -= 4
            elif int(dica) == 2:
                letradica=funcoes.sorteia_letra(paises[resposta]['capital'],restrito)
                restrito.append(letradica)
                dicasdadas.append(['  - Letras da capital: ', letradica])
                vidas -= 3
            elif int(dica) == 3:
                dicasdadas.append(['  - Área: ', paises[resposta]['area']])
                vidas -= 6
                opcoes.remove('3')
                mercadodedicas.pop(mercadodedicas.index('3. Área             - custa 6 tentativas\n'))
            elif int(dica) == 4:
                dicasdadas.append(['  - População: ', paises[resposta]['populacao'], 'pessoas'])
                vidas -= 5
                opcoes.remove('4')
                mercadodedicas.pop(mercadodedicas.index('4. População        - custa 5 tentativas\n'))
            elif int(dica) == 5:
                dicasdadas.append(['  - Continente: ', paises[resposta]['continente']])
                mercadodedicas.pop(mercadodedicas.index('5. Continente       - custa 7 tentativas\n'))
                vidas -= 7
                opcoes.remove('5')
            elif int(dica) == 0:
                continue

    if vidas<=0:
        print('>>> Você perdeu, o país era: ', resposta)
        jogarnovamente=input('\nJogar novamente? [s|n] ')


print('\n\n\nAté a próxima!')
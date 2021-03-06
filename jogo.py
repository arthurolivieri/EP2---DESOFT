import random
from math import *
import funcoes
import dados


print('\n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \n\nComandos:\n    dica       - entra no mercado de dicas\n    desisto    - desiste da rodada\n    inventario - exibe sua posição')

paises=funcoes.normaliza(dados.DADOS)

mercadodedicas=['\nMercado de Dicas',
'----------------------------------------',
'1. Cor da bandeira  - custa 4 tentativas',
'2. Letra da capital - custa 3 tentativas',
'3. Área             - custa 6 tentativas',
'4. População        - custa 5 tentativas',
'5. Continente       - custa 7 tentativas',
'0. Sem dica',
'----------------------------------------']

jogarnovamente='s'

while jogarnovamente=='s':

    resposta=funcoes.sorteia_pais(paises)
    print('\nUm pais foi escolhido, tente adivinhar!')
    
    cores_exibidas=[]
    restrito=[] #cria uma lista de letras restritas para a dica da capital
    vidas=20 #variavel que conta a quantidade de vidas/tentativas restantes
    paisesordenados=[]
    dicasdadas = []
    
    dica = '0'

    dica1=True
    dica2=True
    dica3=True
    dica4=True
    dica5=True
    #booleanos que definem se as dicas já foram usadas

    cores=funcoes.sorteia_cores(resposta)

    opcoes=['1','2','3','4','5','0'] #lista de opcoes de dicas

    while vidas>0: #loop para caso de derrota
        a = 0 #verificador que usei em dicas e desisto

        if vidas != 20:
            print('\nDistâncias:')
            for i in range(len(paisesordenados)):
                if int(paisesordenados[i][1])>10000:
                    print('\033[1;30m    ', paisesordenados[i][1],'km ->',paisesordenados[i][0],'\033[00m')
                elif int(paisesordenados[i][1])>5000:
                    print('\033[0;35m    ', paisesordenados[i][1],'km ->',paisesordenados[i][0],'\033[00m')
                elif int(paisesordenados[i][1])>2000:
                    print('\033[0;31m    ', paisesordenados[i][1],'km ->',paisesordenados[i][0],'\033[00m')
                elif int(paisesordenados[i][1])>1000:
                    print('\033[0;33m    ', paisesordenados[i][1],'km ->',paisesordenados[i][0],'\033[00m')
                else:
                    print('\033[1;34m    ', paisesordenados[i][1],'km ->',paisesordenados[i][0],'\033[00m')
            print('\nDicas:')
            for i in dicasdadas:
                print('')
                for x in range(len(i)):
                    print (i[x],end='')

        if a != 1:
            if vidas == 20:
                print('Você tem\033[0;36m', vidas,'\033[00mtentativa(s)' )
            elif 20 > vidas > 10:
                print('\nVocê tem\033[0;36m', vidas,'\033[00mtentativa(s)' )
            elif vidas>5:
                print('\nVocê tem\033[0;33m', vidas,'\033[00mtentativa(s)' )
            else:
                print('\nVocê tem\033[0;31m', vidas,'\033[00mtentativa(s)' )
        tentativa=input( '\nQual o seu palpite? ')

        #caso de um país desconhecido
        while tentativa not in paises.keys() and tentativa != 'desisto' and tentativa != 'dica' and tentativa != 'inventario':
            print('pais desconhecido')
            tentativa=input('\nQual o seu palpite? ')

        #caso erre e não tenha tentado esse país antes
        if tentativa != resposta and funcoes.esta_na_lista(tentativa,paisesordenados)==False and tentativa != 'desisto' and tentativa != 'dica' and tentativa != 'inventario':
            vidas-=1            
            dist= (int(funcoes.haversine(6371,paises[tentativa]['geo']['latitude'],paises[tentativa]['geo']['longitude'],paises[resposta]['geo']['latitude'],paises[resposta]['geo']['longitude'])))
            paisesordenados = funcoes.adiciona_em_ordem(tentativa,dist,paisesordenados)
        
        #caso acerte
        if tentativa == resposta:
            print('\n*** Parabéns! Você acertou após', 21-vidas ,'tentativas!')
            jogarnovamente=input('\nJogar novamente? [s|n] ')
            break

        #caso desista
        if tentativa == 'desisto':
            desistir = str(input('Tem certeza que deseja desistir da rodada? [s|n]'))
            if desistir == 's':
                print('>>> Que deselegante desistir, o país era:', resposta)
                jogarnovamente=input('\nJogar novamente? [s|n] ')
                break
        
        if tentativa == 'inventario':
            continue

        #se pedir dica
        if tentativa == 'dica':
            a = 1

            opcoes=['0']
            mercadodedicas=['\nMercado de Dicas',
            '----------------------------------------']

            if vidas>4:
                opcoes.append('1')
                mercadodedicas.append('1. Cor da bandeira  - custa 4 tentativas')
            if vidas>3:
                opcoes.append('2')
                mercadodedicas.append('2. Letra da capital - custa 3 tentativas')
            if vidas>6 and dica3==True:
                opcoes.append('3')
                mercadodedicas.append('3. Área             - custa 6 tentativas')
            if vidas>5 and dica4==True:
                opcoes.append('4')
                mercadodedicas.append('4. População        - custa 5 tentativas')
            if vidas>7 and dica5==True:
                opcoes.append('5')
                mercadodedicas.append('5. Continente       - custa 7 tentativas')

            mercadodedicas.append('0. Sem dica')
            mercadodedicas.append('----------------------------------------')

            escolhasuaopcao='Escolha sua opção ['
            for i in opcoes:
                escolhasuaopcao+=i
                escolhasuaopcao+='|'
            escolhasuaopcao=escolhasuaopcao[:-1]
            escolhasuaopcao+=']: '
            #cria uma string que da as opcoes de dicas

            for i in mercadodedicas:
                print(i)
            dica = input(escolhasuaopcao)

            while dica not in opcoes:
                print('Opção inválida')
                dica = input(escolhasuaopcao)

            if int(dica) == 1:
                if dica1==True:
                    cordica=cores[random.randint(0,len(cores)-1)]
                    dicasdadas.append(['  - Cores da bandeira: ', cordica])
                    cores.remove(cordica)
                    vidas -= 4
                    dica1=False
                else:
                    if cores:
                        cordica=cores[random.randint(0,len(cores)-1)]
                        for i in dicasdadas:
                            if '  - Cores da bandeira: ' in i:
                                i.append(', ')
                                i.append(cordica)
                                vidas-=4
                                cores.remove(cordica)
                                if not cores:
                                    opcoes.remove('1')
                                    mercadodedicas.remove('1. Cor da bandeira  - custa 4 tentativas\n')

            elif int(dica) == 2:
                if dica2==True:
                    letradica=funcoes.sorteia_letra(paises[resposta]['capital'],restrito)
                    restrito.append(letradica)
                    dicasdadas.append(['  - Letras da capital: ', letradica])
                    vidas -= 3
                    dica2=False
                else:
                    letradica=funcoes.sorteia_letra(paises[resposta]['capital'],restrito)
                    restrito.append(letradica)
                    for i in dicasdadas:
                        if '  - Letras da capital: ' in i:
                            i.append(', ')
                            i.append(letradica)
                            vidas -= 3

            elif int(dica) == 3:
                dicasdadas.append(['  - Área: ', paises[resposta]['area']])
                vidas -= 6
                dica3=False
                mercadodedicas.pop(mercadodedicas.index('3. Área             - custa 6 tentativas'))
            elif int(dica) == 4:
                dicasdadas.append(['  - População: ', paises[resposta]['populacao'], ' pessoas'])
                vidas -= 5
                dica4=False
                mercadodedicas.pop(mercadodedicas.index('4. População        - custa 5 tentativas'))
            elif int(dica) == 5:
                dicasdadas.append(['  - Continente: ', paises[resposta]['continente']])
                mercadodedicas.pop(mercadodedicas.index('5. Continente       - custa 7 tentativas'))
                vidas -= 7
                dica5=False
            elif int(dica) == 0:
                a = 1
                continue

    if vidas<=0:
        print('>>> Você perdeu, o país era: ', resposta)
        jogarnovamente=input('\nJogar novamente? [s|n] ')


print('\n\n\nAté a próxima!')
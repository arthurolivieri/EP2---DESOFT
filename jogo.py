
import random
from math import *
import funcoes
import dados

tentativas=20

print('\033[36m + \n ============================ \n|                            |\n| Bem-vindo ao Insper Países |\n|                            |\n ==== Design de Software ==== \nComandos:\ndica       - entra no mercado de dicas\ndesisto    - desiste da rodada\ninventario - exibe sua posição'+ '\036[0m')

paises=funcoes.normaliza(dados.DADOS)


resposta=funcoes.sorteia_pais(paises)
tentativa=input('Você tem', tentativas,'\nQual o seu palpite?')
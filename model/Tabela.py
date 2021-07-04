#O Python por si só não possibilita que trabalhemos diretamente com uma váriavel bidimensional, para isso temos que
#...importar a biblioteca numpy para trabalharmos com arrays, biblioteca essa muito utilizada para analise de dados.
import numpy as np

#neste método eu faço o mapeamento das mudanças de estado do meu DFA, as linhas irão representar meus estados e as colunas a entrada do caractere
def matriz():

    #atribui à minha váriavel matriz a minha trabela de transição
    matriz = np.array([['0', '1'],
                       ['1', '0']], dtype=int)

    #retorno minha matriz para poder ser usada por este método em outras classe e métodos quando solicitado
    return matriz
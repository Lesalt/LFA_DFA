#importação das classes e métodos que irei usar, explico cada uma em suas respectivas classes
from regras.Verifica import verifica
from model.Tabela import matriz

#criação do método processa() responsável por cuidar das regras de processamento do problema
def processa(cadeia: str):

    #inicio o o meu DFA no estado 0(comumente chamado de q0), ou seja, o início do meu DFA
    estadoAtual = 0

    #como a leitura da cadeia funciona da extrema esquerda para a extrema direita, eu determino a posição inicial da minha cadeia como 0
    posi = 0

    #aqui eu crio minha tabela de transição dos estados, já pré determinada de acordo com a linguagem, no método matriz() presente no diretório model, irei explicar o método lá
    tabela = matriz()

    #neste laço de repetição do tipo while eu trabalho as regras de mudanças de estados do meu DFA, como as mudanças de
    #...de posição do meu grafo ocorrem de acordo com a leitura da minha cadeia, eu tenho que repetir esse laço enquanto
    #...minha cadeia não estiver no final e isso é determinado pelo teste lógico do laço

    while posi < len(cadeia):

        #aqui determino o estado atual do meu DFA, como o seu estado atual é determinado de acordo com o caractere da cadeia que estiver sendo
        #...analisado eu começo do primeiro caratere da minha cadeia, ou seja, o caractere presente na posição 0. Vale notar que tenho primeiramente
        #...que fazer um cast para int pois utilizarei essa variável para trabalhar com as posições da minha tabela de transição, e para isso eu uso uma função
        #... do Python bastante intuítiva onde logo após a minha variável cadeia que é do tipo string eu informo qual posição dessa variável eu quero retornar atráves
        #...do uso dos colchetes com um parâmetro informando a posição, a string vira praticamente um array unidimencional, o parâmetro passado é a variável posi, que lembrando,
        #...foi inicializada como 0, portando nessa linha atribuo ao estado atual o estado referente ao caractere presente na posição 0 da string, isso na primeira iteração do laço
        #...a posição irá sendo mudada sucessivamente até o final da string de acordo com as iterações

        estadoAtualInt = int(cadeia[posi])

        #nessa linha é onde eu faço o trabalho de mudança do meu estado do meu DFA, ele irá mudar de acordo com minha tabela definida na classe Tabela.
        #...Note que meu estado inicialmente se encontra na linha 0 e a coluna será determinada de acordo com o caractere da minha cadeia que estiver sendo
        #...analisado, determinando assim qual será o estado atual após a primeira iteração.
        estadoAtual = tabela[estadoAtual][estadoAtualInt]

        #como já trabalhei com o presente caractere da cadeia eu preciso agora mudar de posição e aqui eu faço o incremento da posição
        posi = posi + 1
    #após encerrado o laço eu encerro o meu processo de análise da cadeia, verificando se ela válida e retornando o resultado.
    #...Para isso eu utilizo o método verifica() que está na classe Verifica presente neste mesmo diretório, o diretório de regras.
    return verifica(estadoAtual)











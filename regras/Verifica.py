#Neste médodo eu faço a verificação da minha cadeia. Esta verificação é feita tomando como base nossa tabela.
#...como nossa linguagem necessita que a quantidade de números 1 na nossa cadeia seja ímpar, a nossa mudança de
#...estado se dará sempre que entrar um caractare 1 na análise. Caso entre o caractere 1 na primeira iteração do
#...nosso laço o nosso DFA vai para o estado de aceitação que é 1, pois temos uma quantidade ímpar, caso entre outro,
#...ele tem que sair da aceitação, pois agora temos uma quantidade par de caracteres 1, portanto, ele volta para o estado 0
#... irá seguir assim sucessivamente nossa regra. Portanto, podemos concluir que nossa cadeia só será válida caso, após o último
#... caractere analisado, o meu estado final seja o estado 1 que é o estado de aceitação.

#meu método verifica() recebe como parâmetro o estado final que será uma variável do tipo int
def verifica(estadoFinal: int):
    #atribuo à variável o valor 1, pois representará o estado de aceitação
    valido = 1

    #aqui faço um teste lógico para verificar se meu estado final informado no parâmetro do método é 1 ou seja, se ele está na aceitação
    if(estadoFinal == valido):

        #caso esteja na aceitação retorno que a cadeia é válida
        return 'CADEIA VÁLIDA'
    else:

        #caso não esteja na aceitação retorno que a cadeia é inválida
        return 'CADEIA INVÁLIDA'
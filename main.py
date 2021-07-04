#importação das classes e métodos que irei usar, explico cada uma em suas respectivas classes
from regras.Processo import processa
from front.Request import recebe
from front.Response import entrega

#chamada do método recebe() da classe Request presente no diretório front
cadeia = recebe()

#chamada do método entrega() da classe Responde presente no diretório front
#o método entrega() tem como parâmetro o método processa() presente na classe Processo
entrega(processa(cadeia))

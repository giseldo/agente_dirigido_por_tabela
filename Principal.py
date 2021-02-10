from EnumPos import EnumPos
from EnumAcao import EnumAcao
from Util import Util
from Agente import Agente
from Ambiente import Ambiente

ambiente = Ambiente() # um ambiente
agente = Agente() # um agente
util = Util() # uma classe utilitaria para lidar com as imprimir do agente e do ambiente no prompt de comando


def perceber(agente): # uma funcao para perceber 
    percepcao = "" # inicializa percepcao
    if agente.posicao == EnumPos.A.value:
        percepcao = ambiente.tabuleiro[0] # Leitura da sujeira na posicao A
    elif agente.posicao == EnumPos.B.value: 
        percepcao = ambiente.tabuleiro[1] # Leitura da sujeira na posicao A
    return percepcao


def agir(agente, ambiente, acao): # uma funcao para agir sobre o ambiente
    if acao == EnumAcao.Aspirar.value:
        ambiente.limpar(agente.posicao)
        print("O agente Aspirou")
    elif acao == EnumAcao.Esquerda.value:
        agente.posicao = EnumPos.A.value
        print("O agente moveu para a esquerda")
    elif acao == EnumAcao.Direita.value:
        agente.posicao = EnumPos.B.value
        print("o agente moveu para a direita")

# Inicio, o agente inicia na posição A 
util.imprimir(agente, ambiente) # "A, " -> ['Sujo', 'Sujo']

# primeira percepcao
percepcao = perceber(agente)
acao = agente.AGENTE_DIRIGIDO_POR_TABELA(percepcao)
agir(agente, ambiente, acao)
util.imprimir(agente, ambiente) # "A, " -> ['Limpo', 'Sujo']

# segunda percepcao
percepcao = perceber(agente)
acao = agente.AGENTE_DIRIGIDO_POR_TABELA(percepcao)
agir(agente, ambiente, acao)
util.imprimir(agente, ambiente) # "B, " -> ['Limpo', 'Sujo']

# terceira percepcao
percepcao = perceber(agente)
acao = agente.AGENTE_DIRIGIDO_POR_TABELA(percepcao)
agir(agente, ambiente, acao)
util.imprimir(agente, ambiente) # "B, " -> ['Limpo', 'Limpo']


# implemente uma quarta percepcao, lembre de alterar
# percepcao = perceber(agente)
# acao = agente.AGENTE_DIRIGIDO_POR_TABELA(percepcao)
# agir(agente, ambiente, acao)
# util.imprimir(agente, ambiente) 


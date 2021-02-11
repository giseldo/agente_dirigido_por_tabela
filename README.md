# Agente Dirigido por Tabela


Esse programa demonstra um agente bastante trivial que acompanha a sequência de percepções e depois a utiliza para realizar a indexação em uma tabela de
ações, a fim de decidir o que fazer. A tabela representa explicitamente a função do agente que o programa do agente incorpora. Para construir um agente racional desse modo, devemos construir uma tabela que contenha a ação apropriada para todas as sequências de percepções possíveis.

Esse mundo é tão simples que podemos descrever tudo o que acontece; ele também é um mundo inventado e, portanto, podemos criar muitas variações. Esse mundo particular tem apenas dois locais: os quadrados A e B. O agente aspirador de pó percebe em que quadrado está e se existe sujeira no quadrado. Ele pode optar por mover-se para a esquerda, mover-se para a direita, aspirar a sujeira ou não fazer nada. 

PSEUDO-CÓDIGO

```
função AGENTE-DIRIGIDO-POR-TABELA(percepção) retorna uma ação
  variáveis estáticas: 
    percepções, uma sequência, inicialmente vazia
    tabela, uma tabela de ações, indexada por sequências de percepções, inicialmente completamente especificada
  anexar percepção ao fim de percepções
  ação ← ACESSAR(percepções, tabela)
  retornar ação
 ```

Segue o trecho do arquivo Agente.py equivalente ao pseudo código acima.

```
percepcoes = [] # uma sequencia, inicialmente vazia
tabela = {
 "['A, Limpo']":"Direita"
,"['A, Sujo']":"Aspirar"
,"['B, Limpo']":"Esquerda"
,"['B, Sujo']":"Aspirar"
,"['A, Limpo', 'B, Sujo']":"Aspirar"
,"['A, Limpo', 'B, Limpo']":"Esquerda"
,"['A, Sujo', 'A, Limpo']": "Direita"
,"['A, Limpo', 'B, Limpo', 'A, Limpo']":"Direita"
,"['A, Sujo', 'A, Limpo', 'B, Sujo']":"Aspirar"

} # uma tabela de acoes, indexada por sequencias de percepcoes inicialmente completamente especificada


def AGENTE_DIRIGIDO_POR_TABELA(self, percepcao):
    self.percepcoes.append(self.posicao + percepcao) # anexar percepcao ao fim de percepcoes
    acao = self.ACESSAR(self.percepcoes, self.tabela)
    return acao


def ACESSAR(self, percepcoes, tabela):
    return self.tabela[str(self.percepcoes)]
        
```

Para executar

```
python Principal.py
```

Este arquivo pode ser facilmente executado com a IDE na nuvem https://repl.it
Basta selecionar a opção Run no Repl.it

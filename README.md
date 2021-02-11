# Agente Dirigido por Tabela


Esse programa demonstra um agente bastante trivial que acompanha a sequência de percepções e depois a utiliza para realizar a indexação em uma tabela de
ações, a fim de decidir o que fazer. A tabela representa explicitamente a função do agente que o programa do agente incorpora. Para construir um agente racional desse modo, devemos construir uma tabela que contenha a ação apropriada para todas as sequências de percepções possíveis.

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

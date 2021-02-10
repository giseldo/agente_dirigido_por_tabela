from EnumPos import EnumPos


class Agente:
    posicao = EnumPos.A.value
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
    #,"['A, Sujo', 'A, Limpo', 'B, Sujo', 'B, Limpo']":"Esquerda"
    
    } # uma tabela de acoes, indexada por sequencias de percepcoes inicialmente completamente especificada


    def AGENTE_DIRIGIDO_POR_TABELA(self, percepcao):
        self.percepcoes.append(self.posicao + percepcao) # anexar percepcao ao fim de percepcoes
        acao = self.ACESSAR(self.percepcoes, self.tabela)
        return acao


    def ACESSAR(self, percepcoes, tabela):
        return self.tabela[str(self.percepcoes)]






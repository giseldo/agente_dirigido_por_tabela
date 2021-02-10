from EnumEstado import EnumEstado
from EnumPos import EnumPos


class Ambiente:
    
    tabuleiro = [EnumEstado.Sujo.value,EnumEstado.Sujo.value]

    def limpar(self, posicao):
        if posicao == EnumPos.A.value:
            self.tabuleiro[0] = EnumEstado.Limpo.value
        elif posicao == EnumPos.B.value:
            self.tabuleiro[1] = EnumEstado.Limpo.value



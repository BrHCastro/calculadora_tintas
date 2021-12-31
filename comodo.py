class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):  # Metodo construtor da classe (Será executado quando a classe for instânciada.
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property  # Indica que esse método é uma propriedade
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print("O valor informado da largura é inválida!")
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print("O valor informado da profundidade é inválida!")
            exit()
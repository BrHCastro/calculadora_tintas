class Comodo:
    largura: float
    profundidade: float
    altura: float

    def __init__(self, largura, profundidade):  # Metodo construtor da classe (Será executado quando a classe for instânciada.
        self.largura = float(largura)
        self.profundidade = float(profundidade)
        self.altura = 2.9
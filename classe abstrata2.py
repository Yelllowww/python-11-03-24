from abc import ABC, abstractmethod
class Carro(ABC):
    preco_base = 100
    ct = 0
    @classmethod
    def get_ct(cls):
        return cls.ct
    def get_preco_base(cls):
        return cls.preco_base
    def set_preco_base(cls,novo_preco_base):
        cls.preco_base = novo_preco_base
        return novo_preco_base

    def __init__(self,modelo):
        Carro.ct += 1
        self.modelo = modelo
    def get_modelo(self):
        return self.modelo
    def set_modelo(self,novo_modelo):
        self.modelo = novo_modelo
        return novo_modelo
    @abstractmethod
    def preco_diaria(self):
        pass

class Economico(Carro):
    def __init__(self,modelo):
        super().__init__(modelo)
    def preco_diaria(self):
        preco_diaria = self.preco_base + (self.preco_base * 0.05)
        return preco_diaria

class Intermediario(Carro):
    def __init__(self,modelo):
        super().__init__(modelo)
    def preco_diaria(self):
        preco_diaria = self.preco_base + (self.preco_base * 0.1)
        return preco_diaria

if __name__ == '__main__':
    economico1 = Economico("cruze")
    intermediario1 = Intermediario("Corolla")
    print(economico1.preco_diaria())
    print(economico1.get_modelo())
    print(intermediario1.get_modelo())
    print(intermediario1.preco_diaria())
    print(Carro.get_ct())

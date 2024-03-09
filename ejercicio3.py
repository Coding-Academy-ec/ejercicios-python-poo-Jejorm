class Circulo:
    def __init__(self, radio):
        # Asigna el radio proporcionado al atributo 'radio'
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio ** 2

circulo = Circulo(3)
circulo.calcular_area()
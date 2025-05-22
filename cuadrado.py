class cuadrado:

    def area(lado):
        return lado * lado

    def perimetro(lado):
        return lado * 4
    
lado = 5

calArea = cuadrado.area(lado)
calPerimetro = cuadrado.perimetro(lado)

print("Perimetro:",calPerimetro)
print("Area:", calArea)


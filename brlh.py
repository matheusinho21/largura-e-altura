def retangulo(tipoR, largura, altura):
    r = 0
    if tipoR == "Area":
        r= largura * altura
    elif tipoR == "Perimetro":
        r = 2 * (largura + altura)
    return r

def circulo(tipoR, raio):
    r = 0
    if tipoR == "Area":
        r = 3,14 * (raio ** 2)
    elif tipoR == "Perimetro":
        r = 2 * 3,14 * raio
    return r

a = retangulo("Area",15,4.5)
print(f' Area: {a}')

p= retangulo ("Perimetro", 15,4.5)
print(f'Perimetro:{p}')

def verifica_resultado(altura, largura, raio):
    print(f'retangulo Area:{retangulo("Area",largura,altura)}')
    print(f'retangulo Perimetro: {retangulo("perimetro",largura,altura)}')

verifica_resultado(15,6,7,8)

# Crie um algoritímo que leia 3 valores (lados de um triângulo)
# Determine se formam um triâgulo, e se formar verifique se é um equilátero, isósciles ou escaleno

lado1 = float(input("Qual o lado da reta1: "))
lado2 = float(input("Qual o lado da reta2: "))
lado3 = float(input("Qual o lado da reta3: "))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado3 + lado1) > lado2:
    print("Forma um triângulo")

    if lado1 == lado2 == lado3:
        print("Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Isósceles")
    else:
        print("Escaleno")

else:
    print("Não forma um triângulo")
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Dígite a 1° nota "))
nota2 = int(input("Dígite a 2° nota "))
nota3 = int(input("Dígite a 3° nota "))
nota4 = int(input("Dígite a 4° nota "))

media = (nota1 + nota2 + nota3 + nota4)  / 4

print("A média das 4 notas é de: " + str(media))
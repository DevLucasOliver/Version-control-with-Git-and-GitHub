#Programa se a pessoa pode votar ou não

idade = int(input("Qual a sua idade atual?"))
if idade < 16:
    print("Você não pode votar.")
else:
    print("Você pode votar.")

#Par ou impar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Positivo, negativo ou zero
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#Controle de acesso
senha = input("Digite a senha de acesso: ")
if senha == "12345":
    print("Acesso permitido.")
else:
    print("Acesso negado.")

#Maior de 2 números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print("O primeiro número é maior.")
elif num2 > num1:
    print("O segundo número é maior.")
else:
    print("Os números são iguais.")

#Situação de um aluno
nota = float(input("Digite a nota do aluno: "))    
if nota >= 7:
    print("Aluno aprovado.")    
else:    print("Aluno reprovado.")

#Vogal ou consoante
letra = input("Digite uma letra: ")
if letra in "AEIOUaeiou":
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")

#Tabuada de um número
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 20):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#login com while
senha = ""
while senha != "madagascar":
    senha = input("Digite a senha de acesso: ")
print("Acesso permitido.")

#numeros pares de 1 a 50
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
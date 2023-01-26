#condiçoes bool

# nome = input(str("Coloque seu nome: "))
# idade = int(input("Coloque sua idade: "))
#maior_de_idade = idade>=18

# print("É maior: ? ", maior_de_idade)


nome  = 'Carlos'
sobrenome = 'andré'
idade = 26
maior_de_idade = idade>=18
ano_de_nascimento = 2023-idade
print("Ano de nascimento: ", ano_de_nascimento)
print("É maior de idade? ", maior_de_idade)

altura = 1.73
peso = 71

imc = peso / altura**2
print("Seu IMC é: ", imc)

#formatada 

print(f'o Seu IMC é {imc:.2f}')
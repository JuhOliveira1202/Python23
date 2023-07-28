#Exercício 26:
#Escreva uma função conta vogais que recebe o
#nome do ficheiro, lê esse ficheiro linha a linha e
#calcula quantas vezes aparece cada uma das vogais.

ficheiro=open("Lista.txt",'r')
lista=ficheiro.readlines()
ficheiro.close
contador=0
vogal=input("qual a vogal")

for item in lista:
    contador +=item.count(vogal)
print(contador)

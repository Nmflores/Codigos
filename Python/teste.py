import os
os.system("cls")

n1=input("Insira um numero: ")

n2=input("Insira mais um numero: ")

def adicao(x,y):
    resultado=int(x)+int(y)
    return resultado


resultado= adicao(n1,n2)
print("O resultado é " + str(resultado))

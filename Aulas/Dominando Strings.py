curso = "PyThOn"
cursoN = "       PyThOn"
PI = 3.14159
#Upper e lower -> Maiusculo e minusculo tudo
print(curso.upper())
print(curso.lower())
 
#strip -> Remover espaço em branco
print(cursoN.strip())
print(cursoN.lstrip())
print(cursoN.rstrip())

#Junções e centralização -> join e Center
print(curso.center(12, "#"))
print(".".join(curso))

#Formatar strings depois da virgula
print(f"Valor de PI: {PI:.2f}")
#Formatar strings antes da virgula
print(f"Valor de PI: {PI:10.2f}")

#Fatiamento
nome = "Kauhan Gomes Dias Furtado"
print(nome[0])
print(nome[-5])
print(nome[:9])
print(nome[10:])
print(nome[:])
print(nome[7:20:2])
print(nome[::-1])

mensagem = f"""
    Olá meu nome é: {nome},
Eu estou aprendendo python.
    Essa mensagem tem diferentes recuos.
"""
print(mensagem)
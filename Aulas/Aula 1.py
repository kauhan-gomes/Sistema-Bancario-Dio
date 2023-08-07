# =============================================================================
# 1-Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
# =============================================================================


idade = int(input('Digite sua idade: '))

if (idade <= 12):
    print('Você ainda é uma criança')
else:
    if (idade >= 13 and idade < 18):
        print('Você é um adolescente')
    else:
        print(' Você é um adulto')
        

# Calcular a média de um aluno que cursou a disciplina de Programação I,
# a partir da leitura das notas M1, M2 e M3; 
# passando por um cálculo da média aritmética. 
# Após a média calculada, devemos anunciar se o aluno foi aprovado, 
# reprovado ou pegou exame
# - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
# - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
# - Se a média for maior do que 6.0, o aluno está aprovado
# - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado


n1 = float(input(' Digite a primeira nota: '))
n2 = float(input(' Digite a segunda nota: '))
n3 = float(input(' Digite a terceira nota: '))

media = (n1 + n2+ n3)/3

if (media <= 4):
    print('Reprovado')
if (media > 4 and media < 6):
    print('Aluno em exame')
    exame = float(input('Digite a nota do exame: '))
    if (exame > 6):
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado!')
if(media >= 6):
    print('Aluno aprovado')                 
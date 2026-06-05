
CONSTANTE_BONUS = 1000

#O programa deve começar solicitando ao usuário que insira seu nome.
nome_usuario = input("Digite o seu nome: ")

#Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Digite o seu salario:"))

#Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Digite o seu bonus:"))

#O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

valor_do_bonus = CONSTANTE_BONUS  + salario_usuario * bonus_usuario


print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus}")



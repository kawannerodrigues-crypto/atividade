#DESAFIO
#Crie uma calculadora de elegibilidade para beneficio social como axilio jovem aprendiz

#o progama deve

# coletar dados do usuario
# verificar criterios exigidos
# informar se a pessoa pode ou nao receber o beneficio
# Coletando dados do usuário
print("=== Cadastro de Usuário ===")

nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
renda_mensal = float(input("Renda mensal: R$ "))
status = input("Status [estudante/trabalhador/ambos]: ")

# Lista de cidades permitidas
cidades_validas = ["São Paulo", "Campinas", "Salvador", "Recife"]

# Lista de status válidos (estudante ou ambos)
status_validos = ["estudante", "ambos"]

# Estrutura condicional (if) para verificar a elegibilidade
if (14 <= idade <= 24) and (cidade in cid…)




nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.500

dados = {"nome": "Guilherme", "idade": 28,}

print("1° " "Nome: %s Idade: %d" % (nome, idade))

print("2° " "Nome: {} Idade: {}".format(nome, idade))

print("3° " "Nome: {1} Idade: {0}".format(idade, nome))
print("4° " "Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"\nNome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: R$ {saldo:6.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.3f}")

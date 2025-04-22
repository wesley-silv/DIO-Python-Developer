import os
from datetime import datetime

# ===== CONFIGURAÇÕES INICIAIS =====
LIMITE_SAQUE = 500
LIMITE_SAQUES_DIARIOS = 3
extrato = []
saldo = 0
numero_saques = 0

# ===== FUNÇÕES DE SUPORTE =====

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_titulo():
    print("=" * 50)
    print("🏦 Bem-vindo ao Banco Virtual Python".center(50))
    print("=" * 50)

def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        if valor <= 0:
            raise ValueError
        return valor
    except ValueError:
        print("❌ Valor inválido! Informe um número positivo, como '100.00'.")
        return None

def registrar_movimentacao(tipo, valor):
    data = datetime.now().strftime('%d/%m/%Y %H:%M')
    extrato.append(f"{data} - {tipo}: R$ {valor:.2f}")

def mostrar_extrato():
    print("\n📄 EXTRATO".center(50, "="))
    if not extrato:
        print("Nenhuma movimentação registrada até o momento.")
    else:
        for mov in extrato:
            print(mov)
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("=" * 50)

def confirmar_saida():
    confirma = input("Deseja realmente sair? (s/n): ").strip().lower()
    return confirma == 's'

# ===== MENU INTERATIVO =====

menu = """
Escolha uma opção:

[d] Depositar   - Adicionar dinheiro à sua conta
[s] Sacar       - Retirar dinheiro (limite de R$500 por saque)
[e] Extrato     - Ver todas as movimentações
[q] Sair        - Encerrar sessão

=> """

# ===== LOOP PRINCIPAL =====

while True:
    limpar_tela()
    exibir_titulo()
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor_str = input("Informe o valor a depositar: R$ ").strip()
        valor = validar_valor(valor_str)

        if valor:
            saldo += valor
            registrar_movimentacao("Depósito", valor)
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES_DIARIOS:
            print("❌ Limite diário de saques atingido (3 por dia).")
            input("Pressione ENTER para continuar...")
            continue

        valor_str = input("Informe o valor do saque: R$ ").strip()
        valor = validar_valor(valor_str)

        if valor:
            if valor > saldo:
                print("❌ Saldo insuficiente para realizar esta operação.")
            elif valor > LIMITE_SAQUE:
                print(f"❌ O valor excede o limite de saque (R$ {LIMITE_SAQUE:.2f}).")
            else:
                saldo -= valor
                numero_saques += 1
                registrar_movimentacao("Saque", valor)
                print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "e":
        mostrar_extrato()
        input("Pressione ENTER para continuar...")

    elif opcao == "q":
        if confirmar_saida():
            print("\n👋 Sessão encerrada com sucesso. Obrigado por utilizar nosso banco!\n")
            break
        else:
            print("👍 Ok! Continuamos com sua sessão ativa.")

    else:
        print("⚠️ Opção inválida. Por favor, escolha uma opção do menu.")

    input("\nPressione ENTER para voltar ao menu...")

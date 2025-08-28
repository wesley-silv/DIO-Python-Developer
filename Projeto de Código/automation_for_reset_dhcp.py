import subprocess

# Nome da interface de rede - edite conforme sua máquina
INTERFACE = "Wi-Fi"

# Configurações fixas
ips = ["192.168.0.23", "192.168.10.23", "192.168.1.10"]
gateway = "192.168.10.254"
dns = ["8.8.8.8", "8.8.4.4"]

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True)

def configurar_ip():
    print("\n🔹 Aplicando configurações manuais...")
    # Limpa configurações antigas
    run_cmd(f'netsh interface ip set address name="{INTERFACE}" source=dhcp')
    run_cmd(f'netsh interface ip set dns name="{INTERFACE}" source=dhcp')

    # Primeiro IP com gateway
    run_cmd(f'netsh interface ip set address name="{INTERFACE}" static {ips[0]} 255.255.255.0 {gateway} 1')

    # Define DNS primário e secundário
    run_cmd(f'netsh interface ip set dns name="{INTERFACE}" static {dns[0]}')
    run_cmd(f'netsh interface ip add dns name="{INTERFACE}" {dns[1]} index=2')

    # Adiciona IPs adicionais sem gateway
    for ip in ips[1:]:
        run_cmd(f'netsh interface ip add address name="{INTERFACE}" {ip} 255.255.255.0')

    print("\n✅ Configurações aplicadas com sucesso!")

def resetar_dhcp():
    print("\n🔹 Restaurando DHCP...")
    run_cmd(f'netsh interface ip set address name="{INTERFACE}" source=dhcp')
    run_cmd(f'netsh interface ip set dns name="{INTERFACE}" source=dhcp')
    print("\n✅ Configurações de rede resetadas para DHCP.")

if __name__ == "__main__":
    print("===== Automação de Configuração de Rede =====")
    print("1 - Aplicar configuração manual (IP fixo)")
    print("2 - Restaurar para DHCP (padrão)")
    escolha = input("\nEscolha a opção: ")

    if escolha == "1":
        configurar_ip()
    elif escolha == "2":
        resetar_dhcp()
    else:
        print("❌ Opção inválida.")

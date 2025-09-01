import subprocess

# Name of network interface - edit according your machine
INTERFACE = "Wi-Fi"

# Fixe configurations
ips = ["192.168.0.23", "192.168.10.23", "192.168.1.10"]
gateway = "192.168.10.254"
dns = ["8.8.8.8", "8.8.4.4"]

def run_cmd(cmd):
    """Executing commands in Windows and show results in console"""
    print(f"🔹 Executando: {cmd}")
    subprocess.run(cmd, shell=True)

def set_ip():
    """Set IPs statical and DNS"""
    print("\n📌 Aplicando configurações manuais...")
    
    # Clean previously configurations 
    default_dhcp(silent=True)

    # First IP with Gateway
    run_cmd(f'netsh interface ip set address name="{INTERFACE}" static {ips[0]} 255.255.255.0 {gateway} 1')

    # Define DNS primary and secondary
    run_cmd(f'netsh interface ip set dns name="{INTERFACE}" static {dns[0]}')
    run_cmd(f'netsh interface ip add dns name="{INTERFACE}" {dns[1]} index=2')

    # IPs additionals without Gateway
    for ip in ips[1:]:
        run_cmd(f'netsh interface ip add address name="{INTERFACE}" {ip} 255.255.255.0')

    print("\n✅ Configurações aplicadas com sucesso para IP fixo!")

def default_dhcp(silent=False):
    """Return for DHCP default"""
    if not silent:
        print("\n📌 Restaurando DHCP...")
    run_cmd(f'netsh interface ip set address name="{INTERFACE}" source=dhcp')
    run_cmd(f'netsh interface ip set dns name="{INTERFACE}" source=dhcp')
    if not silent:
        print("\n✅ Configurações aplicadas com sucesso para DHCP padrão!")

def menu():
    """Show main menu"""
    print("\n===== Automação Para Configuração De Rede =====")
    print("1 - Aplicar configuração manual (IP fixo)")
    print("2 - Restaurar para DHCP (padrão)")
    print("0 - Sair")

if __name__ == "__main__":
    while True:
        menu()
        escolha = input("\nEscolha a opção: ")

        if escolha == "1":
            set_ip()
        elif escolha == "2":
            default_dhcp()
        elif escolha == "0":
            print("\n✅ Encerrando automação para configuração de rede.")
            break
        else:
            print("❌ Opção inválida! Por favor tente novamente.")
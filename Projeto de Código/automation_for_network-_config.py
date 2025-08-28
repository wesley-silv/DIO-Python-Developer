import subprocess

# Nome da interface de rede Wi-Fi
INTERFACE = "Wi-Fi"

# Configurações
ips = ["192.168.0.23", "192.168.10.23", "192.168.1.10"]
gateway = "192.168.10.254"
dns = ["8.8.8.8", "8.8.4.4"]

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True)

# Remove configurações anteriores (volta para DHCP antes de aplicar fixo)
run_cmd(f'netsh interface ip set address name="{INTERFACE}" source=dhcp')
run_cmd(f'netsh interface ip set dns name="{INTERFACE}" source=dhcp')

# Define o primeiro IP com gateway
run_cmd(f'netsh interface ip set address name="{INTERFACE}" static {ips[0]} 255.255.255.0 {gateway} 1')

# Define DNS primário
run_cmd(f'netsh interface ip set dns name="{INTERFACE}" static {dns[0]}')

# Define DNS secundário
run_cmd(f'netsh interface ip add dns name="{INTERFACE}" {dns[1]} index=2')

# Adiciona os outros IPs sem gateway
for ip in ips[1:]:
    run_cmd(f'netsh interface ip add address name="{INTERFACE}" {ip} 255.255.255.0')

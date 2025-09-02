import os

# Structure for embasement of project
estrutura = {
    "Treasury Automation": [
        "main.py",
        "requirements.txt",
        ".env",
        "README.md",
        {"data": [
            "entradas/",
            "processados/",
            "logs/"
        ]},
        {"src": [
            "autenticacao.py",
            "navegacao.py",
            "formulario.py",
            "extracao.py",
            "seguranca.py",
            "utils.py"
        ]},
        {"tests": [
            "test_autenticacao.py",
            "test_extracao.py",
            "test_seguranca.py"
        ]},
        {"docs": [
            "requisitos.md",
            "arquitetura.md",
            "fluxos.md"
        ]}
    ]
}


def criar_estrutura(base, raiz="."):
    for item in base:
        if isinstance(item, str):
            if item.endswith("/"):
                os.makedirs(os.path.join(raiz, item), exist_ok=True)
            else:
                caminho = os.path.join(raiz, item)
                # Cria arquivo vazio se não existir
                if not os.path.exists(caminho):
                    with open(caminho, "w", encoding="utf-8") as f:
                        f.write("")  
        elif isinstance(item, dict):
            for pasta, conteudo in item.items():
                pasta_path = os.path.join(raiz, pasta)
                os.makedirs(pasta_path, exist_ok=True)
                criar_estrutura(conteudo, pasta_path)


if __name__ == "__main__":
    criar_estrutura(estrutura["Treasury Automation"])
    print("✅ Estrutura de projeto criada com sucesso!")
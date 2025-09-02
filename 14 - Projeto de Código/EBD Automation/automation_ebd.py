import pandas as pd
import requests
import json

ENDPOINT = "https://intregracao-site.presbiterio.org.br/api-ebd/cadastro-contribuicao"

def enviar_participacao(dados):
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.igrejacristamaranata.org.br",
        "Referer": "https://www.igrejacristamaranata.org.br/"
    }
    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(dados))
    return response.status_code, response.json() if response.headers.get("Content-Type") == "application/json" else response.text

def preencher_campos_existentes(dados_excel, dados_site):
    """
    Verifica campo a campo. Se o site já tem dado, mantém; 
    se estiver vazio, pega do Excel.
    """
    payload = {}
    campos = [
        "nome", "cpf", "email", "celular", "denominacao_id", "denominacao_outras",
        "categoria_id", "funcao", "funcao_id", "trabalho_id", "ebd_id",
        "contribuicao", "aceite_termo", "cidade", "uf"
    ]
    for campo in campos:
        valor_site = dados_site.get(campo) if dados_site else None
        valor_excel = dados_excel.get(campo)
        # Se o site não tiver o valor ou estiver vazio, usar o Excel
        payload[campo] = valor_excel if not valor_site else valor_site
    return payload

def processar_participacoes(arquivo_excel):
    df = pd.read_excel(arquivo_excel)
    resultados = []

    for _, row in df.iterrows():
        dados_excel = {
            "nome": row["Nome"],
            "cpf": str(row["CPF"]),
            "email": row["Email"] if pd.notna(row["Email"]) else "",
            "celular": row["Celular"] if pd.notna(row["Celular"]) else "",
            "denominacao_id": int(row["Denominacao_ID"]),
            "denominacao_outras": row["Denominacao_Outras"] if pd.notna(row["Denominacao_Outras"]) else "",
            "categoria_id": str(row["Categoria_ID"]),
            "funcao": row["Funcao"] if pd.notna(row["Funcao"]) else "",
            "funcao_id": str(row["Funcao_ID"]),
            "trabalho_id": str(row["Trabalho_ID"]),
            "ebd_id": str(row["EBD_ID"]),
            "contribuicao": row["Contribuicao"],
            "aceite_termo": bool(row["Aceite_Termo"]),
            "cidade": row["Cidade"],
            "uf": row["UF"]
        }

        # Aqui você poderia fazer uma consulta para verificar dados do CPF
        dados_site = {}  # Ex.: retornar dados do site para este CPF, se houver
        payload = preencher_campos_existentes(dados_excel, dados_site)

        status, resposta = enviar_participacao(payload)
        resultados.append((row["CPF"], status, resposta))

    return resultados

if __name__ == "__main__":
    arquivo = "participacoes_modelo_script.xlsx"
    resultados = processar_participacoes(arquivo)

    for cpf, status, resposta in resultados:
        print(f"CPF: {cpf} | Status: {status} | Resposta: {str(resposta)[:100]}...")

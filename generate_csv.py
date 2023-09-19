import requests
import csv

def get_last_10_users():
    url = 'https://sdw-2023-prd.up.railway.app/users'
    headers = {'accept': '*/*'}

    try:
        response = requests.get(url, headers=headers)

        # Verifica se a resposta da solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            data = response.json()
            # Limita a quantidade de resultados a 10
            limited_data = data[:10]
            return limited_data
        else:
            return f"Erro na solicitação: Código de status {response.status_code}"
    except Exception as e:
        return f"Erro na solicitação: {str(e)}"

def salvar_csv(nome_arquivo, dados):

    try:
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            # Inserir o nome da coluna
            escritor_csv.writerow(['UserID']) 
            # Inserir os dados na coluna 
            for user_id in dados:
                escritor_csv.writerow([user_id]) 
            
        print(f'O arquivo {nome_arquivo} foi gerado com sucesso.')
    except Exception as e:
        print(f"Erro ao gerar o arquivo CSV: {str(e)}")

result = get_last_10_users()
ids = [user_id['id'] for user_id in result]
salvar_csv('SDW2023.csv', ids)

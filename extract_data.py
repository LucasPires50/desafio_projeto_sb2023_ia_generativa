import requests
import json
import pandas as pd

# Gerar DataFrame
df = pd.read_csv('SDW2023.csv')

# Pegar os dados que estão na coluna "UserID" e retorna em uma lista
user_ids = df['UserID'].to_list()
print(user_ids)

def get_user(id):
    url = f'https://sdw-2023-prd.up.railway.app/users/{id}'
    headers = {'accept': '*/*'}

    try:
        response = requests.get(url, headers=headers)

        return response.json() if response.status_code == 200 else f"Erro na solicitação: Código de status {response.status_code}"
    except Exception as e:
        return f"Erro na solicitação: {str(e)}"
    
'''
O operador := é conhecido como "operador de atribuição de expressão" ou "operador walrus". 
Ele foi introduzido no Python 3.8 e permite atribuir valores a variáveis ​​dentro de expressões, 
o que pode tornar o código mais conciso e legível em algumas situações.
'''
# Conceito de compreensão de listas para atrbuição do usuário
# Se for none, não será feito a atrobuição na lista de usuários 
users = [user for id in user_ids if (user := get_user(id)) is not None]

# Imprimir o resultado formatado
print(json.dumps(users, indent=2))
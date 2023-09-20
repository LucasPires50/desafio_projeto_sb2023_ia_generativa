import requests
from transform_data import users

def update_user(user):
    url = f'https://sdw-2023-prd.up.railway.app/users/{user["id"]}'
    headers = {'accept': '*/*'}

    try:
        response = requests.put(url, headers=headers, json=user)

        return response.json() if response.status_code == 200 else f"Erro na solicitação: Código de status {response.status_code}"
    except Exception as e:
        return f"Erro na solicitação: {str(e)}"

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}")
    print("\n")
    
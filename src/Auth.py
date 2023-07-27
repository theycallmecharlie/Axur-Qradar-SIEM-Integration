import requests


class Authentication:
    def __init__(self, MAIL, PASSWORD, TENANT):
        self.mail = MAIL
        self.pw = PASSWORD
        self.tenant = TENANT

    def authenticate(self):
        payload = {
            "email": self.mail,
            "password": self.pw
        }
        header = {
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(
                f"https://api.axur.com/gateway/1.0/api/identity/session", json=payload, headers=header)
            header = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': f'Bearer {response.json()["token"]}'
            }
            TENANT_TOKEN = requests.post(
                f"https://api.axur.com/gateway/1.0/api/identity/customers/{self.tenant}/session", headers=header)
            return TENANT_TOKEN.json()['token']
        except Exception as err:
            print(f"Error: {err}")

import requests


class ZapiService:
    def __init__(
        self,
        instance_id: str,
        instance_token: str,
        instance_client_token: str,
    ):
        self.instance_id = instance_id
        self.instance_token = instance_token
        self.instance_client_token = instance_client_token

    def send_message(self, telefone: str, nome: str):
        url = (
            f"https://api.z-api.io/instances/{self.instance_id}"
            f"/token/{self.instance_token}/send-text"
        )

        message = f"Olá, {nome} tudo bem com você?"

        payload = {
            "phone": telefone,
            "message": message
        }

        headers = {
            "Client-Token": self.instance_client_token,
            "Content-Type": "application/json"
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()
        return response.json()
import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        load_dotenv()

        self.supabase_url = os.getenv("SUPABASE_URL")
        self.supabase_key = os.getenv("SUPABASE_KEY")

        self.zapi_instance_id = os.getenv("ZAPI_INSTANCE_ID")
        self.zapi_instance_token = os.getenv("ZAPI_INSTANCE_TOKEN")
        self.zapi_client_token = os.getenv("ZAPI_CLIENT_TOKEN")


        self._validate()

    def _validate(self):
        required = {
            "SUPABASE_URL": self.supabase_url,
            "SUPABASE_KEY": self.supabase_key,
            "ZAPI_INSTANCE_ID": self.zapi_instance_id,
            "ZAPI_INSTANCE_TOKEN": self.zapi_instance_token,
            "ZAPI_CLIENT_TOKEN": self.zapi_client_token,
        }

        missing = [
            key for key, value in required.items()
            if not value
        ]

        if missing:
            raise EnvironmentError(
                f"Variáveis de ambiente não encontradas no .env: {', '.join(missing)}"
            )
import logging
import requests

from config.settings import Settings
from services.supabase_service import SupabaseService
from services.zapi_service import ZapiService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    settings = Settings()

    supabase_service = SupabaseService(
        settings.supabase_url,
        settings.supabase_key
    )

    contatos = supabase_service.get_contatos()

    zapi_service = ZapiService(
        settings.zapi_instance_id,
        settings.zapi_instance_token,
    )

    if not contatos:
        logging.warning("Nenhum contato encontrado.")
        return

    for contact in contatos:
        nome = contact.get("nome")
        telefone = contact.get("telefone")

        if not nome or not telefone:
            logging.warning(f"Contato inválido ignorado: {contact}")
            continue

        try:
            result = zapi_service.send_message(telefone, nome)
            logging.info(f"Mensagem enviada para {nome} ({telefone}): {result}")
        except requests.exceptions.RequestException as error:
            logging.error(f"Erro ao enviar mensagem para {nome}: {error}")

if __name__ == "__main__":
    main()
from config.settings import Settings
from services.supabase_service import SupabaseService
from services.zapi_service import ZapiService


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
        print("Nenhum contato encontrado.")
        return

    for contact in contatos:
        nome = contact.get("nome")
        telefone = contact.get("telefone")

        result = zapi_service.send_message(telefone, nome)

        print(f"Mensagem enviada para {nome}: {result}")

if __name__ == "__main__":
    main()
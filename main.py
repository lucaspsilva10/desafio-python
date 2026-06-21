from config.settings import Settings
from services.supabase_service import SupabaseService


def main():
    settings = Settings()

    supabase_service = SupabaseService(
        settings.supabase_url,
        settings.supabase_key
    )

    contatos = supabase_service.get_contatos()

if __name__ == "__main__":
    main()
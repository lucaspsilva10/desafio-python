from supabase import create_client, Client


class SupabaseService:
    def __init__(self, supabase_url: str, supabase_key: str):
        self.client: Client = create_client(supabase_url, supabase_key)

    def get_contatos(self):
        response = (
            self.client
            .table("contatos")
            .select("id, nome, telefone")
            .eq("ativo", True)
            .limit(3)
            .execute()
        )

        return response.data
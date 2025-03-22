import os

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase_client: Client = create_client(
    supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY
)

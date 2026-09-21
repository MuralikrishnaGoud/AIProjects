import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR=Path(__file__).resolve().parent
load_dotenv(BASE_DIR/'.env')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY','').strip()
OPENAI_MODEL=os.getenv('OPENAI_MODEL','gpt-5.6-luna').strip()
def require_api_key():
    if not OPENAI_API_KEY or OPENAI_API_KEY == 'your-api-key-here':
        raise RuntimeError('OPENAI_API_KEY is missing. Copy .env.example to .env and add your real API key.')

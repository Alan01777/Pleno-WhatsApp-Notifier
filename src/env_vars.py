import logging
import os
from dotenv import load_dotenv

def load_env_vars():
    load_dotenv('../.env')
    TOKEN = os.getenv("META_TOKEN")
    if not TOKEN:
        logging.warning("META_TOKEN not found in environment variables.")
    return TOKEN
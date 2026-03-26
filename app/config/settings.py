import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", 5))
        self.ENV = os.getenv("ENV", "dev")

settings = Settings()
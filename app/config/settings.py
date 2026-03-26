import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.INTERVAL_SECONDS = int(os.getenv("INTERVAL_SECONDS", 5))
        self.ENV = os.getenv("ENV", "dev")

        self.SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
        self.SLACK_CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

        self.EMAIL_HOST = os.getenv("EMAIL_HOST")
        self.EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
        self.EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
        self.EMAIL_FOLDER = os.getenv("EMAIL_FOLDER", "INBOX")

        self.NOTION_TOKEN = os.getenv("NOTION_TOKEN")
        self.NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

settings = Settings()
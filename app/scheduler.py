import time
from datetime import datetime
from app.digest import DigestService

class Scheduler:
    def __init__(self, interval: int = 30):
        self.interval = interval
        self.digest_service = DigestService()

    def run(self):
        print("\n" + "=" * 50)
        print(f"⏱ {datetime.now()} - Running heartbeat cycle...\n")

        try:
            digest = self.digest_service.generate()
            print(digest)
        except Exception as e:
            print(f" Error: {e}")

    def start(self):
        try:
            while True:
                self.run()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\n Scheduler stopped by user.")
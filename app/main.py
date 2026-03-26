from app.scheduler import Scheduler
from app.config.settings import settings

def main():
    print("🚀 Heartbeat Monitor Started")
    scheduler = Scheduler(interval=settings.INTERVAL_SECONDS)
    scheduler.start()

if __name__ == "__main__":
    main()
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.config.settings import settings

class SlackSource:
    def __init__(self):
        self.client = None
        if settings.SLACK_BOT_TOKEN:
            self.client = WebClient(token=settings.SLACK_BOT_TOKEN)
        self.last_timestamp = None

    def fetch(self):
        if not self.client or not settings.SLACK_CHANNEL_ID:
          
            return self._get_mock_data()

        try:
           
            response = self.client.conversations_history(
                channel=settings.SLACK_CHANNEL_ID,
                limit=10,  # Get last 10 messages
                oldest=self.last_timestamp if self.last_timestamp else None
            )

            messages = []
            for message in response["messages"]:
            
                if message.get("bot_id") or message.get("subtype"):
                    continue

               
                text = message.get("text", "").lower()
                priority = "low"
                if any(keyword in text for keyword in ["urgent", "critical", "blocked", "error", "fail"]):
                    priority = "high"

                messages.append({
                    "message": f"Slack: {message.get('text', '')}",
                    "priority": priority,
                    "timestamp": message.get("ts")
                })

            if response["messages"]:
                self.last_timestamp = response["messages"][0]["ts"]

            return messages

        except SlackApiError as e:
            print(f"Slack API Error: {e}")
            return self._get_mock_data()
        except Exception as e:
            print(f"Slack Error: {e}")
            return self._get_mock_data()

    def _get_mock_data(self):
        return [
            {
                "message": "Client blocked on API issue",
                "priority": "high"
            },
            {
                "message": "Daily standup completed",
                "priority": "low"
            }
        ]
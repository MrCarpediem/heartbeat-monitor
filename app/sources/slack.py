class SlackSource:
    def fetch(self):
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
class EmailSource:
    def fetch(self):
        return [
            {
                "message": "Client requested urgent update on delivery timeline",
                "priority": "high"
            }
        ]
from app.sources.slack import SlackSource
from app.sources.email import EmailSource
from app.sources.notion import NotionSource

class SourceManager:
    def __init__(self):
        self.sources = [
            SlackSource(),
            EmailSource(),
            NotionSource()
        ]

    def collect(self):
        data = []
        for source in self.sources:
            data.extend(source.fetch())
        return data
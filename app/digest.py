from app.sources.manager import SourceManager
from app.utils.classifier import classify
from app.utils.llm import LLMService

class DigestService:
    def __init__(self):
        self.source_manager = SourceManager()
        self.llm = LLMService()

    def generate(self):
        data = self.source_manager.collect()
        urgent, info = classify(data)
        return self.llm.summarize(urgent, info)
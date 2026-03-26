from notion_client import Client
from notion_client.errors import APIResponseError
from app.config.settings import settings

class NotionSource:
    def __init__(self):
        self.client = None
        if settings.NOTION_TOKEN:
            self.client = Client(auth=settings.NOTION_TOKEN)
        self.last_edited_time = None

    def fetch(self):
        if not self.client or not settings.NOTION_DATABASE_ID:
           
            return self._get_mock_data()

        try:
            
            response = self.client.search(
                query="",
                sort={"property": "last_edited_time", "direction": "descending"},
                page_size=10
            )

            messages = []
            for page in response["results"]:
             
                title = self._get_page_title(page)

               
                status = self._get_property_value(page, "Status")

                priority = "low"
                text_to_check = f"{title} {status}".lower()
                if any(keyword in text_to_check for keyword in ["urgent", "critical", "blocked", "review", "pending"]):
                    priority = "high"

                messages.append({
                    "message": f"Notion: {title}" + (f" (Status: {status})" if status else ""),
                    "priority": priority,
                    "last_edited": page["last_edited_time"]
                })

            if response["results"]:
                self.last_edited_time = response["results"][0]["last_edited_time"]

            return messages

        except APIResponseError as e:
            print(f"Notion API Error: {e}")
            return self._get_mock_data()
        except Exception as e:
            print(f"Notion Error: {e}")
            return self._get_mock_data()

    def _get_page_title(self, page):
        """Extract the title from a Notion page"""
        title_property = page["properties"].get("Name") or page["properties"].get("Title")
        if title_property and title_property["type"] == "title":
            title_parts = title_property["title"]
            return "".join([part["plain_text"] for part in title_parts])
        return "Untitled Page"

    def _get_property_value(self, page, property_name):
        """Get a property value from a Notion page"""
        prop = page["properties"].get(property_name)
        if not prop:
            return None

        if prop["type"] == "select":
            return prop["select"]["name"] if prop["select"] else None
        elif prop["type"] == "status":
            return prop["status"]["name"] if prop["status"] else None
        elif prop["type"] == "rich_text":
            return "".join([part["plain_text"] for part in prop["rich_text"]])

        return None

    def _get_mock_data(self):
        return [
            {
                "message": "Task marked as completed in project board",
                "priority": "low"
            }
        ]
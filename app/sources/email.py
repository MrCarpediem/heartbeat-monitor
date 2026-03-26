import imapclient
import email
from email.header import decode_header
from app.config.settings import settings

class EmailSource:
    def __init__(self):
        self.last_uid = None

    def fetch(self):
        if not all([settings.EMAIL_HOST, settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD]):
          
            return self._get_mock_data()

        try:
           
            server = imapclient.IMAPClient(settings.EMAIL_HOST, ssl=True)
            server.login(settings.EMAIL_USERNAME, settings.EMAIL_PASSWORD)
            server.select_folder(settings.EMAIL_FOLDER)

            uids = server.search(['SINCE', '1-Jan-2024'])  
            if self.last_uid:
                uids = [uid for uid in uids if uid > self.last_uid]

            messages = []
            for uid in uids[-10:]:  
                raw_message = server.fetch([uid], ['BODY[]'])
                email_message = email.message_from_bytes(raw_message[uid][b'BODY[]'])

                subject = self._decode_header(email_message.get('Subject', ''))

                sender = self._decode_header(email_message.get('From', ''))

              
                subject_lower = subject.lower()
                priority = "low"
                if any(keyword in subject_lower for keyword in ["urgent", "critical", "emergency", "asap", "important"]):
                    priority = "high"

                messages.append({
                    "message": f"Email from {sender}: {subject}",
                    "priority": priority,
                    "uid": uid
                })

            if uids:
                self.last_uid = max(uids)

            server.logout()
            return messages

        except Exception as e:
            print(f"Email Error: {e}")
            return self._get_mock_data()

    def _decode_header(self, header):
        """Decode email header that might be encoded"""
        decoded_parts = decode_header(header)
        decoded_string = ""
        for part, encoding in decoded_parts:
            if isinstance(part, bytes):
                decoded_string += part.decode(encoding or 'utf-8', errors='ignore')
            else:
                decoded_string += str(part)
        return decoded_string

    def _get_mock_data(self):
        return [
            {
                "message": "Client requested urgent update on delivery timeline",
                "priority": "high"
            }
        ]
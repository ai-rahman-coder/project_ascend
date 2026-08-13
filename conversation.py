import database


class Conversation:

    def __init__(self, user_id):
        self.user_id = user_id

    def add_message(self, role, content):
        database.add_message(
            self.user_id,
            role,
            content
        )

    def get_messages(self):
        rows = database.get_messages(self.user_id)
        messages = []

        for role, content in rows:
            messages.append({
                "role": role,
                "parts": [
                    {
                        "text": content
                    }
                ]
            })
            
        return messages
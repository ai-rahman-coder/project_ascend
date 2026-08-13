import database


class Conversation:

    def add_message(self, role, content):
        database.add_message(role, content)

    def get_messages(self):
        rows = database.get_messages()

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
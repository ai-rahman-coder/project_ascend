import json


class Conversation:

    def __init__(self):
        self.messages = self.load_history()

    def add_message(self, role, content):
        self.messages.append({"role": role, "parts": [{"text": content}]})
        self.save_history()

    def get_messages(self):
        return self.messages

    def load_history(self):
        try:
            with open("conversation.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_history(self):
        with open("conversation.json", "w") as f:
            json.dump(self.messages, f, indent=4)
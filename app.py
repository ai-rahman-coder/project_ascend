from project_ascend.ai_service.gemini_service import ask_ai
from conversation import Conversation

conversations = Conversation()

while True:
    question = input("Ask something (or type 'exit' to quit): ")
    if question.lower() in ['exit', 'quit']:
        break

    conversations.add_message("user", question)
    
    response = ask_ai(conversations.get_messages())
    print("\nAI:", response, "\n")

    conversations.add_message("model", response)

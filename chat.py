import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-3.5-flash-lite"

chat = client.chats.create(model=MODEL_NAME)

print("Chat started. Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    for attempt in range(3):
        try:
            response = chat.send_message(user_input)
            print("AI:", response.text)
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

#if any model gives 500+ error then write this and look for thr model available
# import os
# from dotenv import load_dotenv
# from google import genai

# load_dotenv()
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# for m in client.models.list():
#     actions = getattr(m, "supported_actions", None) or []
#     name = m.name
#     if "generateContent" in actions and "flash" in name \
#        and "live" not in name and "audio" not in name:
#         print(name)
from dotenv import load_dotenv
from google import genai
from google.genai import types

from system_prompt import SYSTEM_PROMPT

load_dotenv()
client = genai.Client()

MODEL = "gemini-3.5-flash"

history = []

print("Kampala Pharmacy Assistant (type 'quit' to exit)")

while True:
    user_input = input("\nYou: ")

    if user_input.strip().lower() == "quit":
        print("Goodbye!")
        break

    if not user_input.strip():
        continue

    history.append(
        types.Content(role="user", parts=[types.Part(text=user_input)])
    )

    reply = ""

    try:
        stream = client.models.generate_content_stream(
            model=MODEL,
            contents=history,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
        )

        print("Bot: ", end="", flush=True)

        for chunk in stream:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                reply += chunk.text

        print()

    except Exception as error:
        history.pop()
        print("\nSorry, something went wrong. Please try again.")
        print("(Details:", error, ")")
        continue

    if not reply:
        history.pop()
        print("Sorry, I could not produce an answer. Please try again.")
        continue

    history.append(
        types.Content(role="model", parts=[types.Part(text=reply)])
    )

    print(f"[debug: {len(history)} messages stored]")
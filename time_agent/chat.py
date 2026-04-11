from google import genai
import os
from agent import root_agent
from dotenv import load_dotenv
load_dotenv()


def main():
    print("=== CMD Chat with Gemini + Your Tools ===")
    print("Type 'exit' to quit.\n")

    # Load your API key from .env or environment
    api_key = os.getenv("GOOGLE_GENAI_API_KEY")

    if not api_key:
        print("ERROR: No API key found. Make sure GOOGLE_GENAI_API_KEY is in your .env file.")
        return

    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.5-flash"

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # IMPORTANT:
        # We manually call the model, AND also call your tools inside agent logic.
        # root_agent.run_prompt orchestrates this automatically for us.
        response = root_agent.run_prompt(user_input)

        print("Agent:", response.text)


if __name__ == "__main__":
    main()

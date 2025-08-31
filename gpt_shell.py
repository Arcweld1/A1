import os
import subprocess
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("The 'google-generativeai' package is required. Install with `pip install google-generativeai`.")
    sys.exit(1)

def main() -> None:
    # Configure Google Generative AI with the provided API key
    api_key = "AIzaSyAeUWiKEIDwHr6EcONJGbjUMzhJr0uujek"
    genai.configure(api_key=api_key)
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-pro')
    
    print("Type instructions for the assistant. Type 'exit' to quit.")

    while True:
        try:
            user = input("\nYou: ")
        except EOFError:
            break

        if user.strip().lower() in {"exit", "quit"}:
            break

        prompt = (
            "You are a helpful assistant that converts natural language into shell commands "
            "for a Unix-like environment. Only return the command itself."
        )

        try:
            # Use Google Generative AI to generate the response
            full_prompt = f"{prompt}\n\nUser request: {user}"
            response = model.generate_content(full_prompt)
            command = response.text.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            continue

        print(f"Assistant suggests: {command}")
        confirm = input("Run this command? [y/N] ").strip().lower()
        if confirm == "y":
            try:
                subprocess.run(command, shell=True, check=True)
            except subprocess.CalledProcessError as exc:
                print(f"Command failed with exit code {exc.returncode}.")

if __name__ == "__main__":
    main()

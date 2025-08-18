import os
import subprocess
import sys

try:
    from openai import OpenAI
except ImportError:
    print("The 'openai' package is required. Install with `pip install openai`.")
    sys.exit(1)

def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set the OPENAI_API_KEY environment variable.")
        return

    client = OpenAI(api_key=api_key)
    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that converts natural language into shell commands "
                "for a Unix-like environment. Only return the command itself."
            ),
        }
    ]

    print("Type instructions for the assistant. Type 'exit' to quit.")

    while True:
        try:
            user = input("\nYou: ")
        except EOFError:
            break

        if user.strip().lower() in {"exit", "quit"}:
            break

        messages.append({"role": "user", "content": user})

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        command = response.choices[0].message.content.strip()
        messages.append({"role": "assistant", "content": command})

        print(f"Running: {command}")
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as exc:
            print(f"Command failed with exit code {exc.returncode}.")

if __name__ == "__main__":
    main()

# A1

This repository includes a small example script, `gpt_shell.py`, that connects to the OpenAI ChatGPT API.
The script accepts natural language instructions, obtains a shell command from the model, and executes it
directly. This demonstrates how you might link a local environment with ChatGPT for command-line assistance
driven entirely by chat prompts.

## Usage

1. Install dependencies:
   ```bash
   pip install openai
   ```
2. Export your API key:
   ```bash
   export OPENAI_API_KEY="<your_api_key>"
   ```
3. Run the script and follow the prompts:
   ```bash
   python gpt_shell.py
   ```

Commands returned by the model are executed automatically, so review your prompts carefully.

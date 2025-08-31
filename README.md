# A1

This repository includes a small example script, `gpt_shell.py`, that connects to the Google Generative AI API (Gemini).
The script accepts natural language input, obtains a shell command suggestion from the model, and optionally
executes it locally. This demonstrates how you might link a local environment with Google's AI for command-line
assistance.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script and follow the prompts:
   ```bash
   python gpt_shell.py
   ```

Commands are only executed after manual confirmation.

Note: The script uses a pre-configured Google API key for Generative AI access.

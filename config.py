import os

# Global application state
# Load the API key from the environment. In the UI, this can be updated.
API_KEY = os.getenv("GEMINI_API_KEY", "")

# If False, process copies automatically. If True, only process when hotkey is pressed.
HOTKEY_ONLY_MODE = False

# Minimum characters required to trigger AI processing (if not a URL)
MIN_TEXT_LENGTH = 100

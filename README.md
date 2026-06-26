    <div align="center">
      <img src="https://lh3.googleusercontent.com/d/1P5uh1B45ayD-WUdkQlRplS-jF--A44zi" width="150" alt="My Project Image">
      <h1>ClipOwl</h1>
      <p><strong>Your brilliant, AI-powered clipboard assistant.</strong></p>
    </div>

    ---

    **ClipOwl** is a sleek, background Windows application that acts as your personal AI reading assistant. Whenever you copy text, code, or a URL to your
  clipboard, ClipOwl silently analyzes it in the background using Google's ultra-fast **Gemini AI** and delivers a concise summary directly to a native Windows
  Desktop Notification.

    ## Features

    - **Instant AI Summarization**: Uses `gemini-2.5-flash` to generate lightning-fast summaries of whatever you copy.
    - **Smart URL Scraping**: Copied a link? ClipOwl automatically downloads the webpage in the background and summarizes the core article.
    - **Privacy Shield Regex Filters**: Automatically detects and blocks sensitive data (Passwords, Credit Cards, API Keys, Crypto Wallets) from ever leaving
  your machine.
    - **Interactive Popups**: Click the Windows notification to open a beautiful, scrollable Dark Mode popup window with your full, unrestricted AI summary.
    - **Hotkey Execution Mode**: Toggle "Hotkey Mode" to stop passive scanning. The AI will only analyze your clipboard when you explicitly press `Ctrl+Alt+S`.
    - **Persistent Configuration**: Enter your API key once. Your settings are securely saved to your local user directory and load seamlessly on startup.
    - **System Tray Integration**: Close the UI and it minimizes cleanly to your Windows System Tray.

    ---

    ## Installation & Setup

    1. Head over to the **[Releases](../../releases)** tab on this GitHub repository.
    2. Download the latest **`ClipOwl_Setup.exe`** file.
    3. Double-click the installer and follow the setup wizard.

    ---

    ## For Developers & Contributors

    If you want to view the source code or build the executable yourself:

    1. Clone the repository.

    2. Install the required dependencies:

       ```bash
       pip install google-genai beautifulsoup4 pyperclip keyboard customtkinter windows-toasts pystray Pillow

  3. Run the application via  python ui.py  or build the executable using PyInstaller:
    pyinstaller --noconsole --onefile --icon=icon.ico --collect-all customtkinter ui.py

  4. Use the included  setup.iss  with Inno Setup to generate the final setup wizard.
  ──────
  ## Built With

  • Google GenAI SDK https://github.com/google/generative-ai-python - For seamless integration with Gemini 2.5 Flash.
  • CustomTkinter https://github.com/TomSchimansky/CustomTkinter - For the modern Dark Mode GUI.
  • Windows-Toasts https://github.com/DatGuy1/Windows-Toasts - For native Windows Action Center notifications with click handlers.
  • Pystray https://github.com/moses-palmer/pystray - For seamless background execution in the system tray.
  • BeautifulSoup https://www.crummy.com/software/BeautifulSoup/ - For automated background web scraping.

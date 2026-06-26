<div align="center">
  <img src="https://lh3.googleusercontent.com/d/1P5uh1B45ayD-WUdkQlRplS-jF--A44zi" width="120" alt="ClipOwl Logo">
  <h1>ClipOwl</h1>
  <p><strong>A lightweight, AI-powered clipboard assistant for Windows.</strong></p>
</div>


---

**ClipOwl** is a background application that acts as a personal reading assistant. Whenever you copy text, code, or a URL to your clipboard, ClipOwl analyzes it in the background using Google's Gemini AI and delivers a concise summary directly via native Windows notifications.

## Features

- **Instant AI Summarization**: Uses `gemini-2.5-flash` to generate swift summaries of copied content.
- **Smart URL Scraping**: Automatically downloads and summarizes the core articles from copied links.
- **Privacy Shield**: Employs regex filters to detect and block sensitive data (passwords, credit cards, API keys, crypto wallets) locally before sending queries to the API.
- **Interactive Popups**: Click the Windows toast notification to open a scrollable, modern dark mode window containing the full, detailed summary.
- **Hotkey Trigger Mode**: Toggle a manual execution mode where ClipOwl only analyzes your clipboard upon pressing `Ctrl+Alt+S`.
- **Persistent Configuration**: Securely saves settings, such as your Gemini API key, locally to load seamlessly on startup.
- **System Tray Integration**: Runs quietly in the system tray when closed, keeping your taskbar clean.

## Installation & Setup

1. Go to the [Releases](../../releases) section of this repository.
2. Download the latest `ClipOwl_Setup.exe`.
3. Run the installer and follow the setup wizard.

## Development

To build the project from source or contribute to its development:

1. Clone the repository.

2. Install the required dependencies:

   ```bash
   pip install google-genai beautifulsoup4 pyperclip keyboard customtkinter windows-toasts pystray Pillow
   ```

3. Run the application directly:

   ```bash
   python ui.py
   ```

4. Build the standalone executable using PyInstaller:

   ```bash
   pyinstaller --noconsole --onefile --icon=icon.ico --collect-all customtkinter ui.py
   ```

5. Generate the final setup wizard using Inno Setup with the provided `setup.iss` configuration.

## Dependencies

- **[Google GenAI SDK](https://github.com/google/generative-ai-python)** - For seamless integration with Gemini 2.5 Flash.
- **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - For the modern Dark Mode GUI.
- **[Windows-Toasts](https://github.com/DatGuy1/Windows-Toasts)** - For native Windows 10/11 Action Center notifications with click action support.
- **[Pystray](https://github.com/moses-palmer/pystray)** - For system tray execution.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** - For automated webpage parsing.


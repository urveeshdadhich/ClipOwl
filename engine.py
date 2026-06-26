import time
import re
import threading
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import pyperclip
import keyboard
from plyer import notification

import config

class SmartClipEngine:
    def __init__(self):
        self.last_clipboard_content = ""
        self.is_running = False

    def is_sensitive(self, text):
        # Implement strict Regex filters
        # API keys
        if re.search(r'(sk-[a-zA-Z0-9]{20,})', text) or re.search(r'(AIza[0-9A-Za-z-_]{35})', text):
            return True
        # Credit card numbers
        if re.search(r'\b(?:\d[ -]*?){13,16}\b', text):
            return True
        return False

    def process_url(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove scripts, styles, nav, etc.
            for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
                element.extract()
            
            # Extract main article headline and body text
            title = soup.title.string if soup.title else ""
            paragraphs = soup.find_all('p')
            body_text = " ".join([p.get_text() for p in paragraphs])
            
            return f"Title: {title}\nContent: {body_text}"
        except Exception as e:
            print(f"Error scraping URL: {e}")
            return None

    def summarize_with_gemini(self, text):
        if not config.API_KEY:
            self.notify("Error", "Gemini API Key is not set. Please set it in Settings.")
            return

        try:
            genai.configure(api_key=config.API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = (
                "You are a quiet, concise clipboard assistant. Summarize the following text. "
                "If it is an article/webpage, provide exactly 3 bullet points. "
                "If it is a block of programming code, explain what it does in exactly 1 clear sentence. "
                "Keep response lengths highly brief for a desktop notification bubble.\n\n"
                f"Text:\n{text}"
            )
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Error generating summary: {e}")
            return "Failed to generate summary."

    def notify(self, title, message):
        try:
            # Handle long strings gracefully
            if len(message) > 256:
                message = message[:253] + "..."
            
            notification.notify(
                title=title,
                message=message,
                app_name="Smart Clip",
                timeout=10
            )
        except Exception as e:
            print(f"Notification error: {e}")

    def process_text(self, text, force=False):
        if not force and config.HOTKEY_ONLY_MODE:
            return

        if not text:
            return

        is_url = text.startswith("http://") or text.startswith("https://")
        
        if not force and not is_url and len(text) < config.MIN_TEXT_LENGTH:
            return

        if self.is_sensitive(text):
            print("Safety Warning: Sensitive data detected. Ignoring clipboard content.")
            self.notify("Safety Warning", "Sensitive data detected. Ignored.")
            return

        content_to_summarize = text
        if is_url:
            scraped_content = self.process_url(text)
            if scraped_content:
                content_to_summarize = scraped_content
            else:
                return

        summary = self.summarize_with_gemini(content_to_summarize)
        if summary:
            self.notify("Smart Clip Summary", summary)

    def force_process(self):
        print("Hotkey pressed: Forcing clipboard processing.")
        text = pyperclip.paste()
        self.process_text(text, force=True)

    def run_loop(self):
        self.is_running = True
        self.last_clipboard_content = pyperclip.paste()
        
        # Register global hotkey
        keyboard.add_hotkey('ctrl+alt+s', self.force_process)
        
        while self.is_running:
            try:
                current_clipboard = pyperclip.paste()
                if current_clipboard != self.last_clipboard_content:
                    self.last_clipboard_content = current_clipboard
                    self.process_text(current_clipboard)
            except Exception as e:
                print(f"Clipboard read error: {e}")
            time.sleep(1) # Sleep to prevent high CPU utilization

def start_engine():
    engine = SmartClipEngine()
    engine_thread = threading.Thread(target=engine.run_loop, daemon=True)
    engine_thread.start()
    return engine

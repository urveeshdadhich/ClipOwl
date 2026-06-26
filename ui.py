import customtkinter as ctk
import threading
import config
from engine import start_engine
import os

class SmartClipUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Clip Settings")
        self.geometry("400x300")
        
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Header
        self.header_label = ctk.CTkLabel(self, text="Smart Clip Settings", font=ctk.CTkFont(size=20, weight="bold"))
        self.header_label.pack(pady=20)

        # API Key Card
        self.api_frame = ctk.CTkFrame(self, corner_radius=10)
        self.api_frame.pack(pady=10, padx=20, fill="x")

        self.api_label = ctk.CTkLabel(self.api_frame, text="Gemini API Key:")
        self.api_label.pack(pady=(10,0), padx=10, anchor="w")

        self.api_entry = ctk.CTkEntry(self.api_frame, show="*", placeholder_text="Enter API Key")
        if config.API_KEY:
            self.api_entry.insert(0, config.API_KEY)
        self.api_entry.pack(pady=10, padx=10, fill="x")

        self.save_button = ctk.CTkButton(self.api_frame, text="Save", command=self.save_api_key)
        self.save_button.pack(pady=(0,10), padx=10)

        # Mode Selection Card
        self.mode_frame = ctk.CTkFrame(self, corner_radius=10)
        self.mode_frame.pack(pady=10, padx=20, fill="x")

        self.hotkey_switch_var = ctk.BooleanVar(value=config.HOTKEY_ONLY_MODE)
        self.hotkey_switch = ctk.CTkSwitch(
            self.mode_frame, 
            text="Only trigger summary on Hotkey (Ctrl+Alt+S)", 
            variable=self.hotkey_switch_var, 
            command=self.toggle_mode
        )
        self.hotkey_switch.pack(pady=15, padx=10)

    def save_api_key(self):
        config.API_KEY = self.api_entry.get()
        print("API Key saved.")

    def toggle_mode(self):
        config.HOTKEY_ONLY_MODE = self.hotkey_switch_var.get()
        print(f"Hotkey only mode set to: {config.HOTKEY_ONLY_MODE}")

if __name__ == "__main__":
    # Start the background engine in a separate daemon thread
    start_engine()
    
    # Run the UI on the main thread
    app = SmartClipUI()
    app.mainloop()

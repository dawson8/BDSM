import customtkinter
from navigation import Navigation
from pages.dashboard_page import Dashboard
from pages.console_page import Console
from pages.settings_page import Settings
from typing import Dict
from bedrock_server_wrapper import BedrockServerWrapper


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.server = BedrockServerWrapper("BDS/bedrock_server.exe", ["-server"])

        self.title("Minecraft Bedrock Dedicated Server Manager")
        self.geometry("800x450")
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        pages: Dict[str, type] = {
            "Dashboard": Dashboard,
            "Console": Console,
            "Settings": Settings,
        }

        self.navigation = Navigation(self, pages)
        self.navigation.grid(row=0, column=0, sticky="nsew")

        self.frames = {}
        for name, page_class in pages.items():
            frame = page_class(self)
            self.frames[name] = frame
            frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame("Dashboard")

    def show_frame(self, page_name: str) -> None:
        frame = self.frames[page_name]
        frame.tkraise()

    def _on_closing(self) -> None:
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

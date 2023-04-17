import customtkinter

from navigation import Navigation
from pages.dashboard_page import Dashboard
from pages.console_page import Console
from pages.settings_page import Settings


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minecraft Bedrock Dedicated Server Manager")
        self.geometry("800x450")
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation = Navigation(self)
        self.navigation.grid(row=0, column=0, sticky="nsew")

        pages = ("Dashboard", "Console", "Settings")

        self.frames = {}
        for PAGE in pages:
            PAGE = eval(PAGE.replace(" ", ""))
            frame = PAGE(self)
            self.frames[PAGE.__name__] = frame

            frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame("Dashboard")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def _on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

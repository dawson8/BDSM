import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minecraft Bedrock Dedicated Server Manager")
        self.geometry("800x450")
        self.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        print("test")

    def _on_closing(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

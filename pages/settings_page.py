import customtkinter


class Settings(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(
            self, parent, fg_color="transparent", corner_radius=0
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = customtkinter.CTkLabel(self, text="Settings")
        label.grid(row=0, column=0, sticky="nsew")

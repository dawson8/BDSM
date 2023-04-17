import customtkinter
from functools import partial


class Navigation(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent, corner_radius=0)

        self.parent = parent

        self.grid_rowconfigure(8, weight=1)

        self.button_list = []

        pages = ("Dashboard", "Console", "Settings")

        for index, page in enumerate(pages):
            button = customtkinter.CTkButton(
                self,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text=page,
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                anchor="w",
                command=partial(self.button_event, index),
            )
            button.grid(row=index, column=0, sticky="ew")

            self.button_list.append(button)

        customtkinter.CTkButton(
            self,
            text="Create",
            command=self.create_button_event,
        ).grid(row=index + 1, column=0, padx=20, pady=20)

        # highlight first button
        self.button_list[0].configure(fg_color=("gray75", "gray25"))

    def button_event(self, index):
        button = self.button_list[index]
        for b in self.button_list:
            b.configure(fg_color=("gray75", "gray25") if b == button else "transparent")

        self.parent.show_frame(button.cget("text"))

    def create_button_event(self):
        print("CREATE")
        self.parent.show_create_server_page()

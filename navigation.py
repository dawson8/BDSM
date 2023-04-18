import customtkinter
from functools import partial


class Navigation(customtkinter.CTkFrame):
    def __init__(self, parent, pages):
        super().__init__(parent, corner_radius=0)

        self.parent = parent

        self.grid_rowconfigure(len(pages), weight=1)

        self.button_list = []
        self.selected_button = None

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
                command=partial(self.button_event, page),
            )
            button.grid(row=index, column=0, sticky="ew")

            self.button_list.append(button)

        # highlight first button
        self.select_button(self.button_list[0])

    def button_event(self, page_name):
        for button in self.button_list:
            if button.cget("text") == page_name:
                self.select_button(button)
                self.parent.show_frame(page_name)
                break

    def select_button(self, button):
        if self.selected_button:
            self.selected_button.configure(fg_color="transparent")
        button.configure(fg_color=("gray75", "gray25"))
        self.selected_button = button

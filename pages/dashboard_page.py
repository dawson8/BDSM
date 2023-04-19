import customtkinter


class Dashboard(customtkinter.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent", corner_radius=0)
        self.parent = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = customtkinter.CTkLabel(self, text="Dashboard")
        label.grid(row=0, column=0, sticky="nsew")

        # Control buttons
        self.control_frame = customtkinter.CTkFrame(self)
        self.start_button = customtkinter.CTkButton(
            self.control_frame, text="Start", command=self.start_server
        )
        self.start_button.grid(row=0, column=0, sticky="nsew")
        self.stop_button = customtkinter.CTkButton(
            self.control_frame, text="Stop", command=self.stop_server
        )
        self.stop_button.grid(row=1, column=0, sticky="nsew")
        self.restart_button = customtkinter.CTkButton(
            self.control_frame, text="Restart", command=self.restart_server
        )
        self.restart_button.grid(row=2, column=0, sticky="nsew")
        self.backup_button = customtkinter.CTkButton(
            self.control_frame, text="Backup", command=self.backup_server
        )
        self.backup_button.grid(row=3, column=0, sticky="nsew")
        self.control_frame.grid(row=1, column=0, sticky="nsew")

        self.status_label = customtkinter.CTkLabel(self, text="Server status: unknown")
        self.status_label.grid(row=2, column=0, sticky="nsew")

        self.update_status()

    def update_status(self):
        status = self.parent.server.get_status()
        self.status_label.configure(text=f"Server status: {status}")
        self.after(1000, self.update_status)

    def start_server(self):
        self.parent.server.start_server()
        self.write_output("Server started")

    def stop_server(self):
        self.parent.server.stop_server()
        self.write_output("Server stopped")

    def restart_server(self):
        self.stop_server()
        self.start_server()

    def backup_server(self):
        backup_path = self.parent.server.backup_server("server_backup.tar.gz")
        self.write_output(f"Backup saved to {backup_path}")

    def write_output(self, text):
        # self.parent.console.write(text)
        print(text)

import customtkinter


def NavigationFrame(self):
    # Navigation Frame
    self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
    self.rowconfigure(0, weight=1)

    self.navigation_frame_label = customtkinter.CTkLabel(
        self.navigation_frame,
        text="Application",
        compound="left",
        font=customtkinter.CTkFont(size=15, weight="bold"),
    )
    self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
    self.navigation_frame.grid(row=0, column=0, sticky="nwse")

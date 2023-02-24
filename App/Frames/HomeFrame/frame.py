import customtkinter


def HomeFrame(self):
    # Home Frame
    self.home_frame = customtkinter.CTkFrame(
        self, corner_radius=10, fg_color="transparent"
    )
    self.home_frame.grid(row=0, column=1, sticky="nwse")
    self.textbox1 = customtkinter.CTkTextbox(self.home_frame, width=250)
    self.textbox1.grid(padx=20, pady=20, sticky="nsew")
    self.textbox1.insert("0.0", "dupa" * 20)
    self.columnconfigure(1, weight=1)

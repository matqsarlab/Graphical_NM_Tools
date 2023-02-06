import os

import customtkinter
from spinbox import FloatSpinbox


class App(customtkinter.CTk):
    # Constants
    WIDTH = 800
    HEIGHT = 600
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
    darkblue = "#1f538d"
    activecolor = "#184270"

    def __init__(self):
        super().__init__()

        self.title("App")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Navigation Frame
        self.NavigationFrame()
        self.NavButtons()

        # # Home Frame
        self.HomeFrame()

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

    def HomeFrame(self):
        # Home Frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=10, fg_color="blue"
        )
        self.home_frame.grid(row=0, column=1, sticky="nwse")
        self.textbox1 = customtkinter.CTkTextbox(self.home_frame, width=250)
        self.textbox1.grid(padx=20, pady=20, sticky="nsew")
        self.textbox1.insert("0.0", "dupa" * 20)
        self.columnconfigure(1, weight=1)

    def DFTFrame(self):
        # create dft frame
        self.dft_frame = customtkinter.CTkFrame(
            master=self,
            corner_radius=10,
            fg_color="transparent",
        )
        self.dft_frame.grid(row=0, column=1, sticky="nwse")
        self.dft_frame.columnconfigure(1, weight=1)
        self.dft_frame.rowconfigure(1, weight=1)
        self.textbox2 = customtkinter.CTkTextbox(self.dft_frame, width=250)
        self.textbox2.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.textbox2.insert(
            "0.0",
            "CTkTextbox\n\n"
            + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n"
            * 200,
        )
        self.textbox3 = customtkinter.CTkTextbox(self.dft_frame, width=250)
        self.textbox3.grid(row=2, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.textbox3.insert("0.0", "Mateusz")

        # Buttons +/-
        self.spinbox_1 = FloatSpinbox(
            self.dft_frame, width=100, step_size=1, default_text="Number of processors"
        )
        self.spinbox_1.grid(padx=20, pady=1, row=0, column=0)
        self.spinbox_1 = FloatSpinbox(
            self.dft_frame, width=100, step_size=1, default_text="RAM [GB]"
        )
        self.spinbox_1.grid(padx=20, pady=1, row=1, column=0)

    def NavButtons(self):
        # Home button
        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="Home",
            # fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="c",
            command=self.home_button_event,
        )
        self.home_button.configure(fg_color=(self.activecolor), state="disabled")
        self.home_button.grid(row=1, column=0, sticky="ew", padx=10)

        # DFT_Button
        self.dft_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=10,
            height=40,
            border_spacing=10,
            text="DFT",
            # fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="c",
            command=self.dft_button_event,
        )
        self.dft_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(
            fg_color=(self.activecolor) if name == "Home" else self.darkblue
        )
        self.dft_button.configure(
            fg_color=(self.activecolor) if name == "DFT" else self.darkblue
        )

        # show selected frame
        if name == "Home":
            self.HomeFrame()
            self.home_button.configure(state="disabled")
        else:
            self.home_frame.grid_forget()
            self.home_button.configure(state="normal")
        if name == "DFT":
            self.DFTFrame()
            self.dft_button.configure(state="disabled")
        else:
            self.dft_frame.grid_forget()
            self.dft_button.configure(state="normal")

    def home_button_event(self):
        self.select_frame_by_name("Home")

    def dft_button_event(self):
        self.select_frame_by_name("DFT")


if __name__ == "__main__":
    app = App()
    app.mainloop()

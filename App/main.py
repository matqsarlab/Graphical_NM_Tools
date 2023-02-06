import os

import customtkinter
from spinbox import FloatSpinbox

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
    # Constants
    WIDTH = 800
    HEIGHT = 800
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
            master=self, corner_radius=10, fg_color="transparent"
        )
        self.dft_frame.grid(row=0, column=1, sticky="nwse")

        # Left Block
        self.leftBlock_frame = customtkinter.CTkFrame(
            master=self.dft_frame,
            corner_radius=10,
            fg_color="transparent",
            height=400,
            width=600,
        )
        self.leftBlock_frame.grid(row=0, column=0, sticky="nwse")

        # Buttons +/-
        self.spinbox_1 = FloatSpinbox(
            self.leftBlock_frame,
            width=100,
            step_size=1,
            default_text="Number of processors",
        )

        self.spinbox_1.grid(padx=20, pady=(50, 0), row=0, column=0, sticky="we")

        self.spinbox_2 = FloatSpinbox(
            self.leftBlock_frame,
            width=100,
            step_size=4,
            default_text="RAM [GB]",
            default_val=16,
        )
        self.spinbox_2.grid(padx=20, pady=(20, 0), row=1, column=0, sticky="we")

        self.spinbox_3 = FloatSpinbox(
            self.leftBlock_frame,
            width=100,
            step_size=0,
            default_text="Charge",
        )
        self.spinbox_3.grid(padx=20, pady=(20, 0), row=2, column=0, sticky="we")

        self.spinbox_4 = FloatSpinbox(
            self.leftBlock_frame,
            width=100,
            step_size=1,
            default_text="Multiplicity",
        )
        self.spinbox_4.grid(padx=20, pady=(20, 0), row=3, column=0, sticky="we")

        # Rigth Block
        self.rightBlock_frame = customtkinter.CTkFrame(
            master=self.dft_frame, corner_radius=10, fg_color="transparent"
        )
        self.rightBlock_frame.grid(row=0, column=1, sticky="nwse")

        # TextBox
        self.textbox2 = customtkinter.CTkTextbox(
            self.rightBlock_frame, width=250, height=400
        )
        self.textbox2.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="ew")
        self.textbox2.insert(
            "0.0",
            "CTkTextbox\n\n"
            + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n"
            * 200,
        )
        self.rightBlock_frame.columnconfigure(1, weight=1)

        self.DFTFrame_buttons()

        # Constant height and weight for left & right blocks
        self.dft_frame.rowconfigure(0, weight=1)
        self.dft_frame.columnconfigure(1, weight=1)

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

    def DFTFrame_buttons(self):
        self.dupa_button = customtkinter.CTkButton(
            master=self.leftBlock_frame,
            fg_color="green",
        )
        self.dupa_button.grid(row=5, column=0, sticky="es", pady=(20, 10))

        self.dupa_button2 = customtkinter.CTkButton(
            master=self.rightBlock_frame,
            width=250,
            fg_color="green",
        )
        self.dupa_button2.grid(
            row=6,
            column=1,
            padx=(20, 20),
            pady=(20, 0),
            sticky="es",
        )

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

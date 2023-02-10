import os
import tkinter

import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green


class App(customtkinter.CTk):
    # Constants
    WIDTH = 860
    HEIGHT = 800
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
    darkblue = "#1f538d"
    activecolor = "#184270"

    # Packages Load:
    from Buttons.NavigationFrame.buttons import NavButtons
    from Frames.DFTFrame.frame import DFTFrame
    from Frames.DipoleFrame.frame import DipoleFrame
    from Frames.HomeFrame.frame import HomeFrame
    from Frames.NavigationFrame.frame import NavigationFrame
    from Frames.selector import select_frame_by_name

    def __init__(self, DFTFrame=DFTFrame, DipoleFrame=DipoleFrame):
        super().__init__()
        self.__DFTFrame__ = DFTFrame
        self.__DipoleFrame__ = DipoleFrame
        self._active_dft_frame = False
        self._active_dipole_frame = False
        self._xyz = "XYZ Structure..."
        self._check_var = tkinter.StringVar(master=self, value="off")

        self.title("QSAR LApp")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Navigation Frame
        self.NavigationFrame()
        self.NavButtons()

        # # Home Frame
        self.HomeFrame()

    def home_button_event(self):
        self.select_frame_by_name("Home")

    def dft_button_event(self):
        self.select_frame_by_name("DFT")

    def dipole_xyz_structure_button_event(self):
        self.select_frame_by_name("DxyzS")


if __name__ == "__main__":
    app = App()
    app.mainloop()

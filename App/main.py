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
    HEIGHT = 850
    CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
    darkblue = "#1f538d"
    activecolor = "#184270"

    # Packages Load:
    from Buttons.NavigationFrame.buttons import NavButtons
    from Frames.DescriptorsFrame.frame import DescriptorsFrame
    from Frames.DFTFrame.frame import DFTFrame
    from Frames.DipoleFrame.frame import DipoleFrame, DipoleFrame2
    from Frames.DipoleMakerFrame.frame import DipoleFrame2x, DipoleFramex
    from Frames.HomeFrame.frame import HomeFrame
    from Frames.NavigationFrame.frame import NavigationFrame
    from Frames.selector import select_frame_by_name
    from Static._dft_read import dft_info

    def __init__(self, dft_info=dft_info):
        super().__init__()
        self.__InitPath__ = ...
        self._active_dft_frame = False
        self._active_dipole_frame = False
        self._active_dipole_maker_frame = False
        self._active_descriptors_frame = False
        self._xyz = "XYZ Structure..."
        self._choose_pseudo_potential = tkinter.StringVar(
            master=self, value="Pseudo Potential"
        )
        self._dipole = None
        self._name = None
        self._line_txt_descriptors_console = None
        self._check_var = tkinter.StringVar(master=self, value="off")
        self._optionmenu_var = tkinter.IntVar(master=self, value=0)  # set initial value
        self._optionmenu_dipole_maker = tkinter.IntVar(
            master=self, value=0
        )  # set initial value
        self._optionmenu_descriptors = tkinter.IntVar(
            master=self, value=0
        )  # set initial value
        self._files_DFT = ""
        self._basis_sets = [
            "3-21G",
            "4-31G",
            "4-31G*",
            "4-31G**",
            "6-21G",
            "6-21G*",
            "6-21G**",
            "6-31G",
            "6-31++G*",
            "6-311G",
            "D95",
            "D95V",
            "SHC",
            "SHC*",
            "CEP-4G",
            "CEP-4G*",
            "CEP-31G",
            "CEP-31G*",
            "CEP-121G",
            "CEP-121G*",
            "LanL2MB",
            "LanL2DZ",
            "SDD, SDDAll",
            "cc-pVDZ",
            "cc-pVTZ",
            "cc-pVQZ",
            "cc-pV5Z",
            "cc-pV6Z",
            "SV",
            "SVP",
            "TZV",
            "TZVP",
            "QZVP",
            "Def2",
            "MidiX",
            "EPR-II",
            "EPR-III",
            "UGBS",
            "MTSmall",
            "DGDZVP",
            "DGDZVP2",
            "DGTZVP",
            "CBSB7",
        ]
        self._pseudopotential = ["LanL2DZ", "LANL1", "LANL2", "--"]
        self._name = {}
        self._consoleText = dft_info()
        self._froze = tkinter.StringVar(master=self, value="off")
        self._default_method = """#p b3lyp gen SCF=(xqc,Tight,intrep,NoVarAcc,Maxcycle=512) GFInput
     IOp(6/7=3) symm=loose  int=(grid=ultrafine) scrf=(solvent=water) pop=(mk,nbo)"""
        self._default_method_dipole = """#p b3lyp gen SCF=(xqc,Tight,intrep,NoVarAcc,Maxcycle=512) GFInput
     IOp(6/7=3) charge   iop(1/6=100)  symm=loose  int=(grid=ultrafine)"""
        self._descriptors_atom_indexes = "atom indexes = \na1 = \na2 = \nb1 = \nb2 = "
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

    def dipole_maker_button_event(self):
        self.select_frame_by_name("dipolemaker")

    def descriptors_button_event(self):
        self.select_frame_by_name("descriptors")


if __name__ == "__main__":
    app = App()
    app.mainloop()

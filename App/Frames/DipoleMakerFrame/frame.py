import tkinter

import customtkinter

from Buttons.DipoleMakerFrame.buttons import DipoleFrame_buttons, buttons2
from Buttons.spinbox import FloatSpinbox
from Static._dft_read import dipole_info

height = 600


def DipoleFramex(self, height=height):
    self._structure1 = tkinter.StringVar(master=self, value="Basis set for Structure 1")
    self._structure2 = tkinter.StringVar(master=self, value="Basis set for Structure 2")
    # create dft frame
    self.dipole_maker_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.dipole_maker_frame.grid(row=0, column=1, sticky="nwse")

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.dipole_maker_frame, width=250, height=350
    )
    self.consoletextbox.grid(
        row=7,
        column=0,
        padx=(20, 20),
        pady=(10, 20),
        sticky="wse",
        columnspan=2,
    )
    self.consoletextbox.insert(
        "0.0",
        dipole_info(),
    )
    self.consoletextbox.configure(state="disabled")

    # Left Block
    self.leftBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_maker_frame,
        corner_radius=10,
        fg_color="transparent",
        height=height,
        width=600,
    )
    self.leftBlock_frame.grid(row=0, column=0, sticky="nwe")

    # Buttons +/-
    self._spinboxN = 0  # row counter for buttons in left block

    self.spinbox_1 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Number of processors",
        default_val=8,
    )

    self.spinbox_1.grid(
        padx=20, pady=(50, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    self.spinbox_2 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=4,
        default_text="RAM [GB]",
        default_val=16,
    )
    self.spinbox_2.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    self.spinbox_3 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Charge",
        default_val=0,
    )
    self.spinbox_3.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    self.spinbox_4 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Multiplicity",
    )
    self.spinbox_4.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    self.spinbox_5 = customtkinter.CTkOptionMenu(
        self.leftBlock_frame,
        variable=self._structure1,
        values=self._basis_sets,
        width=256,
    )
    self.spinbox_5.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    # Rigth Block
    self.rightBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_maker_frame, corner_radius=10, fg_color="transparent"
    )
    self.rightBlock_frame.grid(row=0, column=1, sticky="nwse")

    # TextBox
    self.textbox2 = customtkinter.CTkTextbox(
        self.rightBlock_frame, width=250, height=300
    )
    self.textbox2.grid(
        row=0, column=1, padx=(20, 20), pady=(20, 0), columnspan=2, sticky="ew"
    )
    self.textbox2.insert(
        "0.0",
        "CTkTextbox\n\n" + "dipole" * 200,
    )
    self.rightBlock_frame.columnconfigure(1, weight=1)

    self._spinboxN += 1
    buttons2(self)

    # Constant height and weight for left & right blocks
    self.dipole_maker_frame.rowconfigure(0, weight=1)
    self.dipole_maker_frame.columnconfigure(1, weight=1)


def DipoleFrame2x(self, height=height):
    # create dft frame
    self.dipole_maker_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.dipole_maker_frame.grid(row=0, column=1, sticky="nwse")

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.dipole_maker_frame, width=250, height=350
    )
    self.consoletextbox.grid(
        row=7,
        column=0,
        padx=(20, 20),
        pady=(10, 20),
        sticky="wse",
        columnspan=2,
    )
    self.consoletextbox.insert(
        "0.0",
        self._consoleText,
    )
    self.consoletextbox.configure(state="disabled")

    # Left Block
    self.leftBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_maker_frame,
        corner_radius=10,
        fg_color="transparent",
        height=height,
        width=296,
    )
    self.leftBlock_frame.grid(row=0, column=0, sticky="nwe")

    # Buttons +/-
    self._spinboxN = 0  # row counter for buttons in left block

    # Rigth Block
    self.rightBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_maker_frame, corner_radius=10, fg_color="transparent"
    )
    self.rightBlock_frame.grid(row=0, column=1, sticky="nwse")

    # TextBox
    self.textbox2 = customtkinter.CTkTextbox(
        self.rightBlock_frame, width=250, height=300
    )
    self.textbox2.grid(
        row=0, column=1, padx=(20, 20), pady=(20, 0), columnspan=2, sticky="ew"
    )
    self.textbox2.insert(
        "0.0",
        "CTkTextbox\n\n" + "dipole2 " * 200,
    )
    self.rightBlock_frame.columnconfigure(1, weight=1)

    self._spinboxN += 1
    DipoleFrame_buttons(self)

    # Constant height and weight for left & right blocks
    self.dipole_maker_frame.rowconfigure(0, weight=1)
    self.dipole_maker_frame.columnconfigure(1, weight=1)

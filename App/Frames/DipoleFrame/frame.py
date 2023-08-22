import tkinter

import customtkinter
from Buttons.DipoleFrame.buttons import DipoleFrame_buttons, buttons2
from Buttons.spinbox import FloatSpinbox
from Static._dft_read import dft_info
from Static.tooltips import BasisSet, GeneralButtons

height = 600


def DipoleFrame(self, height=height):
    self._structure1 = tkinter.StringVar(master=self, value="Basis set for Material")
    self._structure2 = tkinter.StringVar(master=self, value="Basis set for Molecule")
    # create dft frame
    self.dipole_xyz_structure_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.dipole_xyz_structure_frame.grid(row=0, column=1, sticky="nwse")

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.dipole_xyz_structure_frame, width=250, height=350
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
        dft_info(method=self._default_method),
    )
    self.consoletextbox.configure(state="disabled")

    # Left Block
    self.leftBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_xyz_structure_frame,
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
    GeneralButtons(button="nproc").tooltip(button=self.spinbox_1)
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
    GeneralButtons(button="ram").tooltip(button=self.spinbox_2)
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
    GeneralButtons(button="charge").tooltip(button=self.spinbox_3)
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
    GeneralButtons(button="multiplicity").tooltip(button=self.spinbox_4)
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
    BasisSet(switcher="s1").tooltip(button=self.spinbox_5)
    self._spinboxN += 1
    self.spinbox_6 = customtkinter.CTkOptionMenu(
        self.leftBlock_frame, variable=self._structure2, values=self._basis_sets
    )
    self.spinbox_6.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    BasisSet(switcher="s2").tooltip(button=self.spinbox_6)
    self._spinboxN += 1

    # Rigth Block
    self.rightBlock_frame = customtkinter.CTkFrame(
        master=self.dipole_xyz_structure_frame, corner_radius=10, fg_color="transparent"
    )
    self.rightBlock_frame.grid(row=0, column=1, sticky="nwse")

    # TextBox
    self.textbox2 = customtkinter.CTkTextbox(
        self.rightBlock_frame, width=250, height=300, wrap="word"
    )
    self.textbox2.grid(
        row=0, column=1, padx=(20, 20), pady=(20, 0), columnspan=2, sticky="ew"
    )
    self.textbox2.insert(
        "0.0",
        "Material-Molecule\n\n"
        + " This section allows you to load two structures - a crystalline material and a"
        + " common molecule (e.g. glycine) then move and rotate them relative to each other in "
        + " a beneficial and predetermined way. The shift and rotation algorithm is based on determining"
        + " the most extreme groups in the nanomaterial and molecule. Remember to select the nanomaterial"
        + " wall in relation to which the molecule will be set - the selection is made by appropriate preparation"
        + " (rotation) of the `*xyz` file with the material structure."
        + "\n\nFurthermore, it allows you to set up a information about method and"
        + " computing power required to make a Gaussian input file in next sub-section `Gaussian Input Creator`"
        + " A set of buttons allows you to easily declare the number of processors, RAM, charge and the"
        + " multiplicity of the considered system, as well as the choice of the basis set for material"
        + " and for molecule. In addition, it is possible to edit the predefined"
        + " calculation method in the `Route` section using the Edit button."
        + "\n\nUsing this method produces three output files: the coordinates file with the extension `xyz`,"
        + " the `atom_info` file which contains the information on which lines matrial/molecule starts and ends,"
        + " and the 'dft_info' containing the `Route` section with information about the method, and other required"
        + " information (such as basis set for material and molecules)."
        + "\n\n More information in the manual.",
    )
    self.textbox2.configure(state="disabled")

    self.rightBlock_frame.columnconfigure(1, weight=1)

    self._spinboxN += 1
    buttons2(self)

    # Constant height and weight for left & right blocks
    self.dipole_xyz_structure_frame.rowconfigure(0, weight=1)
    self.dipole_xyz_structure_frame.columnconfigure(1, weight=1)


def DipoleFrame2(self, height=height):
    # create dft frame
    self.dipole_xyz_structure_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.dipole_xyz_structure_frame.grid(row=0, column=1, sticky="nwse")

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.dipole_xyz_structure_frame, width=250, height=350
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
        master=self.dipole_xyz_structure_frame,
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
        master=self.dipole_xyz_structure_frame, corner_radius=10, fg_color="transparent"
    )
    self.rightBlock_frame.grid(row=0, column=1, sticky="nwse")

    # TextBox
    self.textbox2 = customtkinter.CTkTextbox(
        self.rightBlock_frame, width=250, height=300, wrap="word"
    )
    self.textbox2.grid(
        row=0, column=1, padx=(20, 20), pady=(20, 0), columnspan=2, sticky="ew"
    )
    self.textbox2.insert(
        "0.0",
        "Gaussian Input Creator\n\n"
        + "It allows you to make Gaussian input files using `xyz`, `atom_info` and 'dft_info' files."
        + "In addition, the `Froze` button allows you to freeze the atoms of the material in the input file.",
    )
    self.textbox2.configure(state="disabled")
    self.rightBlock_frame.columnconfigure(1, weight=1)

    self._spinboxN += 1
    DipoleFrame_buttons(self)

    # Constant height and weight for left & right blocks
    self.dipole_xyz_structure_frame.rowconfigure(0, weight=1)
    self.dipole_xyz_structure_frame.columnconfigure(1, weight=1)

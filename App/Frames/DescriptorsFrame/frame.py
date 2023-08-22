import tkinter

import customtkinter
from Buttons.DescriptorsFrame.buttons import DescriptorsFrame_buttons
# DescriptorsFrame_buttons_All)
from Buttons.spinbox import FloatSpinbox
from Static.create_console import insert_txt
from Static.tooltips import GeneralButtons

height = 600


def DescriptorsFrame(self, height=height):
    self._structure1 = tkinter.StringVar(master=self, value="Basis set for Structure 1")
    # create dft frame
    self.descriptors_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.descriptors_frame.grid(row=0, column=1, sticky="nwse")

    # Left Block
    self.leftBlock_frame = customtkinter.CTkFrame(
        master=self.descriptors_frame,
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
        default_text="Number of rotable bonds",
        default_val=0,
    )
    GeneralButtons(button="nrotbonds").tooltip(button=self.spinbox_1)

    self.spinbox_1.grid(
        padx=20, pady=(50, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1
    self.spinbox_2 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Molecular roughness",
        default_val=0,
    )
    GeneralButtons(button="roughness").tooltip(button=self.spinbox_2)

    self.spinbox_2.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1
    self.spinbox_3 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Number of atoms",
        default_val=0,
    )
    GeneralButtons(button="natoms").tooltip(button=self.spinbox_3)

    self.spinbox_3.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1
    self.spinbox_4 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Number of lone-pair-donor",
        default_val=0,
    )
    GeneralButtons(button="nlonepair").tooltip(button=self.spinbox_4)

    self.spinbox_4.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1
    self.spinbox_5 = FloatSpinbox(
        self.leftBlock_frame,
        width=100,
        step_size=1,
        default_text="Number of sp2 carbon atoms",
        default_val=0,
    )
    GeneralButtons(button="nsp2atoms").tooltip(button=self.spinbox_5)
    self.spinbox_5.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.descriptors_frame, width=250, height=350
    )
    self.consoletextbox.grid(
        row=7,
        column=0,
        padx=(20, 20),
        pady=(10, 20),
        sticky="wse",
        columnspan=2,
    )
    insert_txt(self)
    self.consoletextbox.configure(state="disabled")

    # Rigth Block
    self.rightBlock_frame = customtkinter.CTkFrame(
        master=self.descriptors_frame, corner_radius=10, fg_color="transparent"
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
        "Descriptors Calculator"
        "\n\nThis section allows you to calculate several descriptors based on the Gaussian `*.log` output file."
        " First, you need to set information about the surface fragment under consideration using the buttons on the"
        " left side of the panel. In the next step, you need to specify which atoms are part of the surface (e.g. 1-24,"
        " 30, 32, 40-44 -> `Atom Indexes` button) and specify the vectors (A = [a1,a2], B = [b1,b2] - where a1, a2, b1,"
        " b2 are the numbers"
        " of atoms), in such a way that the area stretched between these vectors (A x B = Surface Area) is as close"
        " to real as possible."
        "\n\nAn example setting of the `Atom indexes` section may look like this:"
        "\n\n----------------------------------------------"
        "\natom indexes = 1-24, 30, 32, 40-44"
        "\na1 = 1"
        "\na2 = 8"
        "\nb1 = 24"
        "\nb2 = 13"
        "\n----------------------------------------------"
        "\n\nThe result `qsarlab.descr` file contains information about the descriptors values calculated per"
        " surface area.",
    )
    self.textbox2.configure(state="disabled")
    self.rightBlock_frame.columnconfigure(1, weight=1)

    self._spinboxN += 1
    DescriptorsFrame_buttons(self)

    # Constant height and weight for left & right blocks
    self.descriptors_frame.rowconfigure(0, weight=1)
    self.descriptors_frame.columnconfigure(1, weight=1)

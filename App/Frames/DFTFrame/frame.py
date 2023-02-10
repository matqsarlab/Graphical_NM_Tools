import customtkinter

from Buttons.DFTFrame.buttons import DFTFrame_buttons
from Buttons.spinbox import FloatSpinbox
from Static._dft_read import dft_read


def DFTFrame(self):
    # create dft frame
    self.dft_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="transparent"
    )
    self.dft_frame.grid(row=0, column=1, sticky="nwse")

    # Console TextBox
    self.consoletextbox = customtkinter.CTkTextbox(
        self.dft_frame, width=250, height=350
    )
    self.consoletextbox.grid(
        row=5,
        column=0,
        padx=(20, 20),
        pady=(10, 20),
        sticky="wse",
        columnspan=2,
    )
    self.consoletextbox.insert(
        "0.0",
        dft_read(xyz=self._xyz),
    )
    self.consoletextbox.configure(state="disabled")

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
        self.leftBlock_frame, values=["Basis-1", "Basis-2"]
    )
    self.spinbox_5.grid(
        padx=20, pady=(20, 0), row=self._spinboxN, column=0, sticky="we"
    )
    self._spinboxN += 1

    # Rigth Block
    self.rightBlock_frame = customtkinter.CTkFrame(
        master=self.dft_frame, corner_radius=10, fg_color="transparent"
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
        "CTkTextbox\n\n"
        + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n"
        * 200,
    )
    self.rightBlock_frame.columnconfigure(1, weight=1)

    DFTFrame_buttons(self)

    # Constant height and weight for left & right blocks
    self.dft_frame.rowconfigure(0, weight=1)
    self.dft_frame.columnconfigure(1, weight=1)

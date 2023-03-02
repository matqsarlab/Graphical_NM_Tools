import customtkinter

from Buttons.DescriptorsFrame.Events.button_event import (openSfiles,
                                                          optionmenu_callback,
                                                          saveSfiles,
                                                          viewButtonFunc)
from Buttons.DipoleFrame.Events.button_event import edit_method


def DescriptorsFrame_buttons(self):

    self.view_button = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="green",
        text="View",
        command=lambda: viewButtonFunc(self, self._line_txt_descriptors_console),
    )
    self.view_button.grid(
        row=self._spinboxN, column=0, sticky="es", padx=20, pady=(20, 10)
    )
    self.method = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="#b36b00",
        text="Atom indexes",
        command=lambda: edit_method(self, self._descriptors_atom_indexes),
        width=80,
    )
    self.method.grid(row=self._spinboxN, column=0, sticky="ws", padx=20, pady=(20, 10))
    self._spinboxN += 1

    self.miniframe = customtkinter.CTkFrame(
        self.descriptors_frame, fg_color="transparent"
    )
    self.miniframe.grid(row=4, column=0, sticky="ws", columnspan=6)
    self.chooser1 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Descriptors Creator",
        value=0,
        variable=self._optionmenu_descriptors,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser1.grid(row=0, column=0, sticky="w", padx=25)

    self.chooser2 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Input Creator",
        value=1,
        variable=self._optionmenu_descriptors,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser2.grid(row=1, column=0, sticky="ws", padx=25, pady=(5, 0))

    self.s1 = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=150,
        text="Gaussian log file",
        command=lambda: openSfiles(self, "descriptor"),
    )
    self.s1.grid(
        row=6,
        column=1,
        padx=(20, 20),
        pady=(10, 0),
        sticky="es",
    )

    self.save_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="green",
        text="Save",
        command=lambda: saveSfiles(self),
        state="disabled",
    )
    self.save_button.grid(
        row=6,
        column=2,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )


def DescriptorsFrame_buttons_All(self):

    self.miniframe = customtkinter.CTkFrame(
        self.descriptors_frame, fg_color="transparent"
    )
    self.miniframe.grid(row=5, column=0, sticky="ws")
    self.chooser1 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Coordinates Creator",
        value=0,
        variable=self._optionmenu_descriptors,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser1.grid(row=0, column=0, sticky="w", padx=25)

    self.chooser2 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Gaussian Input Creator",
        value=1,
        variable=self._optionmenu_descriptors,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser2.grid(row=1, column=0, sticky="ws", padx=25, pady=(5, 0))

    self.open_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="#1f538d",
        text="Open...",
        # command=lambda: openToGaussianDir(self),
    )
    self.open_button.grid(
        row=6,
        column=1,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )
    self.frozen_box = customtkinter.CTkCheckBox(
        self.rightBlock_frame,
        text="Froze",
        width=50,
        variable=self._froze,
        onvalue="on",
        offvalue="off",
        # command=lambda: froze_button(self),
    )
    self.frozen_box.grid(row=6, column=1, sticky="w", padx=(20, 20), pady=(20, 0))
    self.frozen_box.lower(belowThis=self.open_button)

    self.save_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="green",
        text="Save",
        # command=lambda: gaussianInputCreator(self),
        state="disabled",
    )
    self.save_button.grid(
        row=6,
        column=2,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )

    if self._xyz != "XYZ Structure...":
        self.save_button.configure(state="normal")

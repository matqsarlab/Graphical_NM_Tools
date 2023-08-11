import customtkinter
from Buttons.DipoleFrame.Events.button_event import edit_method
from Buttons.DipoleMakerFrame.Events.button_event import (dipoleFile,
                                                          froze_button,
                                                          gaussianInputCreator,
                                                          openSfiles,
                                                          openToGaussianDir,
                                                          optionmenu_callback,
                                                          saveSfiles,
                                                          viewButtonFunc2)
from Static.tooltips import Edit, Froze, Material, Open, Save, View


def buttons2(self):
    self.view_button = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="green",
        text="View",
        command=lambda: viewButtonFunc2(self),
    )
    self.view_button.grid(
        row=self._spinboxN, column=0, sticky="es", padx=20, pady=(20, 10)
    )
    View().tooltip(self.view_button)
    self.method = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="#b36b00",
        text="Edit",
        command=lambda: edit_method(self, self._default_method_dipole),
        width=80,
    )
    self.method.grid(row=self._spinboxN, column=0, sticky="ws", padx=20, pady=(20, 10))
    Edit().tooltip(self.method)
    self._spinboxN += 1

    self.miniframe = customtkinter.CTkFrame(
        self.dipole_maker_frame, fg_color="transparent"
    )
    self.miniframe.grid(row=5, column=0, sticky="ws")
    self.chooser1 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Coordinates Creator",
        value=0,
        variable=self._optionmenu_dipole_maker,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser1.grid(row=0, column=0, sticky="w", padx=25)

    self.chooser2 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Gaussian Input Creator",
        value=1,
        variable=self._optionmenu_dipole_maker,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser2.grid(row=1, column=0, sticky="ws", padx=25, pady=(5, 0))

    self.s1 = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=150,
        text="Material Structure...",
        command=lambda: openSfiles(self),
    )
    self.s1.grid(
        row=6,
        column=1,
        padx=(20, 20),
        pady=(10, 0),
        sticky="es",
    )
    Material().tooltip(self.s1)

    self.s2 = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=150,
        text="Dipole...",
        command=lambda: dipoleFile(self),
    )
    self.s2.grid(
        row=7,
        column=1,
        padx=(20, 20),
        pady=(10, 0),
        sticky="es",
    )
    Material(switcher="dipole").tooltip(self.s2)

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
    Save(switcher="xyz").tooltip(self.save_button)

    if self._name:
        pass


def DipoleFrame_buttons(self):
    self.miniframe = customtkinter.CTkFrame(
        self.dipole_maker_frame, fg_color="transparent"
    )
    self.miniframe.grid(row=5, column=0, sticky="ws")
    self.chooser1 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Coordinates Creator",
        value=0,
        variable=self._optionmenu_dipole_maker,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser1.grid(row=0, column=0, sticky="w", padx=25)

    self.chooser2 = customtkinter.CTkRadioButton(
        master=self.miniframe,
        text="Gaussian Input Creator",
        value=1,
        variable=self._optionmenu_dipole_maker,
        command=lambda: optionmenu_callback(self),
    )
    self.chooser2.grid(row=1, column=0, sticky="ws", padx=25, pady=(5, 0))

    self.open_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="#1f538d",
        text="Open...",
        command=lambda: openToGaussianDir(self),
    )
    self.open_button.grid(
        row=6,
        column=1,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )
    Open().tooltip(self.open_button)
    self.frozen_box = customtkinter.CTkCheckBox(
        self.rightBlock_frame,
        text="Froze",
        width=50,
        variable=self._froze,
        onvalue="on",
        offvalue="off",
        command=lambda: froze_button(self),
    )
    self.frozen_box.grid(row=6, column=1, sticky="w", padx=(20, 20), pady=(20, 0))
    self.frozen_box.lower(belowThis=self.open_button)
    Froze().tooltip(self.frozen_box)

    self.save_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="green",
        text="Save",
        command=lambda: gaussianInputCreator(self),
        state="disabled",
    )
    self.save_button.grid(
        row=6,
        column=2,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )
    Save(switcher="com").tooltip(self.save_button)

    if self._xyz != "XYZ Structure...":
        self.save_button.configure(state="normal")

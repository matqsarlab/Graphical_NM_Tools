import customtkinter

from Buttons.DipoleMakerFrame.Events.button_event import (dipoleFile,
                                                          gaussianInputCreator,
                                                          openSfiles,
                                                          openToGaussianDir,
                                                          optionmenu_callback,
                                                          saveSfiles,
                                                          viewButtonFunc2)


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
        text="Crystal Structure...",
        command=lambda: openSfiles(self),
    )
    self.s1.grid(
        row=6,
        column=1,
        padx=(20, 20),
        pady=(10, 0),
        sticky="es",
    )

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
        fg_color="green",
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

    if self._xyz != "XYZ Structure...":
        self.save_button.configure(state="normal")

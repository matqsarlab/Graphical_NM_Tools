import customtkinter

from Buttons.DescriptorsFrame.Events.button_event import (openXYZfiles,
                                                          optionmenu_callback,
                                                          viewButtonFunc,
                                                          xyz2gaussian_save)
from Buttons.DipoleFrame.Events.button_event import edit_method


def DescriptorsFrame_buttons(self):

    self.view_button = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="green",
        text="View",
        # command=lambda: viewButtonFunc2(self),
    )
    self.view_button.grid(
        row=self._spinboxN, column=0, sticky="es", padx=20, pady=(20, 10)
    )
    self.method = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="#b36b00",
        text="Edit",
        command=lambda: edit_method(self, self._default_method),
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
        text="Structures 1...",
        # command=lambda: openSfiles(self, "s1"),
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
        text="Structures 2...",
        # command=lambda: openSfiles(self, "s2"),
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
        # command=lambda: saveSfiles(self),
        state="disabled",
    )
    self.save_button.grid(
        row=6,
        column=2,
        padx=(20, 20),
        pady=(20, 0),
        sticky="es",
    )

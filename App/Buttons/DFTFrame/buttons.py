import customtkinter

from Buttons.DFTFrame.Events.button_event import (openXYZfiles, viewButtonFunc,
                                                  xyz2gaussian_save)


def DFTFrame_buttons(self):

    self.view_button = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="green",
        text="View",
        # command=self.viewButtonFunc,
        command=lambda: viewButtonFunc(self),
    )
    self.view_button.grid(
        row=self._spinboxN, column=0, sticky="es", padx=20, pady=(20, 10)
    )

    self.open_button = customtkinter.CTkButton(
        master=self.rightBlock_frame,
        width=100,
        fg_color="green",
        text="Open...",
        command=lambda: openXYZfiles(self),
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
        command=lambda: xyz2gaussian_save(self),
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

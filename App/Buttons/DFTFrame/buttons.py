import customtkinter
from Buttons.DFTFrame.Events.button_event import (openXYZfiles, viewButtonFunc,
                                                  xyz2gaussian_save)
from Buttons.DipoleFrame.Events.button_event import edit_method
from Buttons.DipoleMakerFrame.Events.button_event import froze_button
from Static.tooltips import Edit, Froze, Open, Save, View


def DFTFrame_buttons(self):
    self.view_button = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="green",
        text="View",
        command=lambda: viewButtonFunc(self),
    )
    self.view_button.grid(
        row=self._spinboxN, column=0, sticky="es", padx=20, pady=(20, 10)
    )
    View().tooltip(self.view_button)
    self.method = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="#b36b00",
        text="Edit",
        command=lambda: edit_method(self, self._default_method),
        width=80,
    )
    self.method.grid(row=self._spinboxN, column=0, sticky="ws", padx=20, pady=(20, 10))
    Edit().tooltip(self.method)

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
    Save(switcher="com").tooltip(self.save_button)

    if self._xyz != "XYZ Structure...":
        self.save_button.configure(state="normal")

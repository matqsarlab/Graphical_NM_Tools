import customtkinter
from Buttons.DescriptorsFrame.Events.button_event import (openSfiles,
                                                          saveSfiles,
                                                          viewButtonFunc)
from Buttons.DipoleFrame.Events.button_event import edit_method
from Static.tooltips import AtomIdx, Open, Save, View


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
    View(switcher="case2").tooltip(button=self.view_button)
    self.method = customtkinter.CTkButton(
        master=self.leftBlock_frame,
        fg_color="#b36b00",
        text="Atom indexes",
        command=lambda: edit_method(self, self._descriptors_atom_indexes),
        width=80,
    )
    AtomIdx().tooltip(button=self.method)
    self.method.grid(row=self._spinboxN, column=0, sticky="ws", padx=20, pady=(20, 10))
    self._spinboxN += 1

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
    Open(switcher="log").tooltip(button=self.s1)

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
    Save(switcher="descr").tooltip(button=self.save_button)

    if self._xyz != "XYZ Structure...":
        self.save_button.configure(state="normal")

import customtkinter


def DipoleFrame(self):
    # create dft frame
    self.dipole_xyz_structure_frame = customtkinter.CTkFrame(
        master=self, corner_radius=10, fg_color="red"
    )
    self.dipole_xyz_structure_frame.grid(row=0, column=1, sticky="nwse")

def select_frame_by_name(self, name):
    # set button color for selected button
    self.home_button.configure(
        fg_color=(self.activecolor) if name == "Home" else self.darkblue
    )
    self.dft_button.configure(
        fg_color=(self.activecolor) if name == "DFT" else self.darkblue
    )
    self.dipole_xyz_structure_button.configure(
        fg_color=(self.activecolor) if name == "DxyzS" else self.darkblue
    )

    # show selected frame
    if name == "Home":
        self.HomeFrame()
        self.home_button.configure(state="disabled")
    else:
        self.home_frame.grid_forget()
        self.home_button.configure(state="normal")
    if name == "DFT":
        self._active_dft_frame = True
        self.DFTFrame()
        self.dft_button.configure(state="disabled")
    else:
        if self._active_dft_frame:
            self.dft_frame.grid_forget()
        self.dft_button.configure(state="normal")
    if name == "DxyzS":
        self._active_dipole_frame = True
        self.DipoleFrame()
        self.dipole_xyz_structure_button.configure(state="disabled")
    else:
        if self._active_dipole_frame:
            self.dipole_xyz_structure_frame.grid_forget()
        self.dipole_xyz_structure_button.configure(state="normal")

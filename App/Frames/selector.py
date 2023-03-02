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
    self.dipole_maker_button.configure(
        fg_color=(self.activecolor) if name == "dipolemaker" else self.darkblue
    )
    self.descriptors_button.configure(
        fg_color=(self.activecolor) if name == "descriptors" else self.darkblue
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
        match self._optionmenu_var.get():
            case 0:
                self.DipoleFrame()
            case 1:
                self.DipoleFrame2()
        self.dipole_xyz_structure_button.configure(state="disabled")

    else:
        if self._active_dipole_frame:
            self.dipole_xyz_structure_frame.grid_forget()
        self.dipole_xyz_structure_button.configure(state="normal")
    if name == "dipolemaker":
        self._active_dipole_maker_frame = True
        match self._optionmenu_dipole_maker.get():
            case 0:
                self.DipoleFramex()
            case 1:
                self.DipoleFrame2x()
        self.dipole_maker_button.configure(state="disabled")

    else:
        if self._active_dipole_maker_frame:
            self.dipole_maker_frame.grid_forget()
        self.dipole_maker_button.configure(state="normal")
    if name == "descriptors":
        self._active_descriptors_frame = True
        match self._optionmenu_descriptors.get():
            case 0:
                self.DescriptorsFrame()
            case 1:
                self.DescriptorsFrame2()
        self.descriptors_button.configure(state="disabled")
    else:
        if self._active_descriptors_frame:
            self.descriptors_frame.grid_forget()
        self.descriptors_button.configure(state="normal")
        self._line_txt_descriptors_console = None

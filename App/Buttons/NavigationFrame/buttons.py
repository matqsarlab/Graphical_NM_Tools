import customtkinter


def NavButtons(self):
    # Home button
    self.home_button = customtkinter.CTkButton(
        self.navigation_frame,
        corner_radius=10,
        height=40,
        border_spacing=10,
        text="Home",
        # fg_color="transparent",
        text_color=("gray10", "gray90"),
        hover_color=("gray70", "gray30"),
        anchor="c",
        command=self.home_button_event,
    )
    self.home_button.configure(fg_color=(self.activecolor), state="disabled")
    self.home_button.grid(row=1, column=0, sticky="ew", padx=10, pady=(0, 10))

    # DFT_Button
    self.dft_button = customtkinter.CTkButton(
        self.navigation_frame,
        corner_radius=10,
        height=40,
        border_spacing=10,
        text="Gaussian Input\nCreator",
        text_color=("gray10", "gray90"),
        hover_color=("gray70", "gray30"),
        anchor="c",
        command=self.dft_button_event,
    )
    self.dft_button.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))

    # Create XYZ with dipole Button
    self.dipole_xyz_structure_button = customtkinter.CTkButton(
        self.navigation_frame,
        corner_radius=10,
        height=40,
        border_spacing=10,
        text="Material-Molecule",
        text_color=("gray10", "gray90"),
        hover_color=("gray70", "gray30"),
        anchor="c",
        command=self.dipole_xyz_structure_button_event,
    )
    self.dipole_xyz_structure_button.grid(
        row=3, column=0, sticky="ew", padx=10, pady=(0, 10)
    )
    # Create XYZ with dipole Button
    self.dipole_maker_button = customtkinter.CTkButton(
        self.navigation_frame,
        corner_radius=10,
        height=40,
        border_spacing=10,
        text="Dipole-Material\nInteraction",
        text_color=("gray10", "gray90"),
        hover_color=("gray70", "gray30"),
        anchor="c",
        command=self.dipole_maker_button_event,
    )
    self.dipole_maker_button.grid(row=4, column=0, sticky="ew", padx=10, pady=(0, 10))

    # Descriptors
    self.descriptors_button = customtkinter.CTkButton(
        self.navigation_frame,
        corner_radius=10,
        height=40,
        border_spacing=10,
        text="Descriptors",
        text_color=("gray10", "gray90"),
        hover_color=("gray70", "gray30"),
        anchor="c",
        command=self.descriptors_button_event,
    )
    self.descriptors_button.grid(row=5, column=0, sticky="ew", padx=10, pady=(0, 10))

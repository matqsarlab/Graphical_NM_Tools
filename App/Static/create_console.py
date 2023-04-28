def insert_txt(self, *args):
    self.consoletextbox.insert(
        "0.0",
        self._descriptors_atom_indexes
        + "\n\n"
        + f"Number of rotable bonds         = {self.spinbox_1.get()}\n"
        + f"Molecular roughness                = {self.spinbox_2.get()}\n"
        + f"Number of atoms                      = {self.spinbox_3.get()}\n"
        + f"Number of lone pair donor       = {self.spinbox_4.get()}\n"
        + f"Number of sp2 carbon atoms  = {self.spinbox_5.get()}\n\n"
        + "*" * 50,
    )
    if self._line_txt_descriptors_console != None:
        self.consoletextbox.insert(
            "end",
            self._line_txt_descriptors_console[0],
            self._line_txt_descriptors_console[1],
        )

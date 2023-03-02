def insert_txt(self):
    self.consoletextbox.insert(
        "0.0",
        self._descriptors_atom_indexes
        + "\n\n"
        + f"Number of rotable bonds = {self.spinbox_1.get()}\n"
        + f"Number of rotable bonds = {self.spinbox_2.get()}\n"
        + f"Number of rotable bonds = {self.spinbox_3.get()}\n"
        + f"Number of rotable bonds = {self.spinbox_4.get()}\n"
        + f"Number of rotable bonds = {self.spinbox_5.get()}\n\n"
        + "*" * 50
        + "\n\n",
    )

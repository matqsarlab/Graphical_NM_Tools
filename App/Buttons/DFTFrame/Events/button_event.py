from customtkinter import filedialog, os

from Static._dft_read import dft_read


def __block__(xyz):
    res = []
    for line in xyz:
        spl = line.split()
        res.append(
            "{}{:>8}{:>12}{:>13}{:>13}\n".format(spl[0], "-1", spl[1], spl[2], spl[3])
        )
    return res


def viewButtonFunc(self):
    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis = str(self.spinbox_5.get())
    pseudo = str(self.spinbox_6.get())
    if self._files_DFT:
        check_name = os.path.basename(self._files_DFT[0]).split(".")[0]
    else:
        check_name = "base_name"

    txt = dft_read(
        nproc,
        ram,
        check_name,
        charge,
        multiplicity,
        basis,
        xyz=self._xyz,
        method=self._default_method,
        pseudo=pseudo,
    )

    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")


def xyz2gaussian_save(self):
    dirName = filedialog.askdirectory(initialdir=self.__InitPath__)

    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis = str(self.spinbox_5.get())
    pseudo = str(self.spinbox_6.get())

    for element in self._files_DFT:
        check_name = os.path.basename(element).split(".")[0]
        o = open(element)
        self._xyz = o.readlines()[2:]
        if self._froze.get() == "on":
            self._xyz = __block__(self._xyz)
        self._xyz = "".join(self._xyz)
        o.close()

        txt = dft_read(
            nproc,
            ram,
            check_name,
            charge,
            multiplicity,
            basis,
            self._xyz,
            self._default_method,
            pseudo=pseudo,
        )

        with open(os.path.join(dirName, check_name + ".com"), "w") as f:
            f.write(txt)


def openXYZfiles(self):

    self._files_DFT = filedialog.askopenfilenames()
    o = open(self._files_DFT[0])
    self._xyz = o.readlines()[2:]
    if self._froze.get() == "on":
        self._xyz = __block__(self._xyz)
    self._xyz = "".join(self._xyz)
    o.close()

    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis = str(self.spinbox_5.get())
    check_name = os.path.basename(self._files_DFT[0]).split(".")[0]

    txt = dft_read(
        nproc,
        ram,
        check_name,
        charge,
        multiplicity,
        basis,
        self._xyz,
        self._default_method,
    )

    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")

    self.save_button.configure(state="normal")

    self.__InitPath__ = os.path.dirname(self._files_DFT[0])

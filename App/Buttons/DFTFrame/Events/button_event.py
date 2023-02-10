from customtkinter import filedialog
from Static._dft_read import dft_read


def viewButtonFunc(self):
    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis = str(self.spinbox_5.get())

    txt = dft_read(nproc, ram, charge, multiplicity, basis, xyz=self._xyz)

    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")


def xyz2gaussian_save(self):
    fileName = filedialog.asksaveasfilename()
    txt = self.consoletextbox.get("0.0", "end")
    with open(fileName, "w") as f:
        f.write(txt)


def openXYZfiles(self):
    _f = filedialog.askopenfilename()
    o = open(_f)
    self._xyz = o.readlines()[2:]
    self._xyz = "".join(self._xyz)
    o.close()

    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis = str(self.spinbox_5.get())

    txt = dft_read(nproc, ram, charge, multiplicity, basis, self._xyz)

    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")

    self.save_button.configure(state="normal")

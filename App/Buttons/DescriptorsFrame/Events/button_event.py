import os
import re

import customtkinter
from customtkinter import filedialog

from Static._dft_read import dft_read
from Static.calc_descriptors import Calc
from Static.create_console import insert_txt


def viewButtonFunc(self, *args):
    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    insert_txt(self, args)
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

    txt = dft_read(
        nproc, ram, charge, multiplicity, basis, self._xyz, self._default_method
    )

    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")

    self.save_button.configure(state="normal")


def optionmenu_callback(self):
    self.select_frame_by_name("descriptors")


def openSfiles(self, name):
    self._name[name] = filedialog.askopenfilename()
    self.__InitPath__ = os.path.dirname(self._name[name])
    self.save_button.configure(state="normal")
    self.s1.configure(fg_color="green")

    fname, ext = os.path.splitext(self._name[name])

    temp = self.consoletextbox.get("0.0", "end")
    idx = [i for i, item in enumerate(temp) if re.search("^[***]", item)][-1]
    temp = temp[: idx + 1]

    if ext == ".log":
        customtkinter.CTkTextbox.tag_config(
            self.consoletextbox, "agree", foreground="green"
        )
        self.consoletextbox.configure(state="normal")
        self.consoletextbox.delete("0.0", "end")
        self.consoletextbox.insert("0.0", temp)
        self.consoletextbox.insert(
            "end", f"\n\n{fname}\t\t\t it's .log file: OK\n", "agree"
        )
        self._line_txt_descriptors_console = (
            f"\n\n{fname}\t\t\t it's .log file: OK\n",
            "agree",
        )
        self.consoletextbox.insert("end", "\n\n")
    else:
        customtkinter.CTkTextbox.tag_config(
            self.consoletextbox, "warning", foreground="#e6ac00"
        )
        self.consoletextbox.configure(state="normal")
        self.consoletextbox.delete("0.0", "end")
        self.consoletextbox.insert("0.0", temp)
        self.consoletextbox.insert(
            "end", f"\n\n{fname}\t\t\t it's not .log file\n", "warning"
        )
        self._line_txt_descriptors_console = (
            f"\n\n{fname}\t\t\t it's not .log file\n",
            "warning",
        )
        self.consoletextbox.insert("end", "\n\n")
    self.consoletextbox.configure(state="disabled")
    del temp


def saveSfiles(self):
    darkblue = "#1f538d"

    dir_path = filedialog.askdirectory(initialdir=self.__InitPath__)
    file = self._name["descriptor"]

    n_rot_bond = str(self.spinbox_1.get())
    n_gropu = str(self.spinbox_2.get())
    n_pair_donor = str(self.spinbox_3.get())
    sp2_carb = str(self.spinbox_4.get())
    n_atoms = str(self.spinbox_5.get())

    lines = self._descriptors_atom_indexes.split("\n")
    a1 = lines[1].replace("a1 = ", "").replace("\n", "").replace(" ", "")
    b1 = lines[2].replace("a2 = ", "").replace("\n", "").replace(" ", "")
    a2 = lines[3].replace("b1 = ", "").replace("\n", "").replace(" ", "")
    b2 = lines[4].replace("b2 = ", "").replace("\n", "").replace(" ", "")

    instance = Calc(file, a1, a2, b1, b2)
    print(instance.area)

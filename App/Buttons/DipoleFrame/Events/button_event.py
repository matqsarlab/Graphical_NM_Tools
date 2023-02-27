import os
import re

import customtkinter
import numpy as np
from customtkinter import filedialog

from Static._dft_read import dft_info
from Static.Align_two_3D_object import (Structure1_translate,
                                        Structure2_add_rotate)


def openSfiles(self, name):
    self._name[name] = filedialog.askopenfilenames()
    self.__InitPath__ = os.path.dirname(self._name[name][0])
    if len(self._name.keys()) > 1:
        self.save_button.configure(state="normal")
    if name == "s1":
        self.s1.configure(fg_color="green")
    if name == "s2":
        self.s2.configure(fg_color="green")


def saveSfiles(self):
    def save(xyz, name, path):
        with open(os.path.join(dir, sub_dir1, sub_dir2, path), "w") as f:
            f.write(str(len(xyz)) + "\n")
            f.write("XYZ file generated by Script\n")
            for coor, n in zip(xyz, name):
                f.write("{}{:>20}{:>13}{:>13}\n".format(n, coor[0], coor[1], coor[2]))

    def atom_info(xyz1, xyz2, sub_dir1, sub_dir2):
        num1 = len(xyz1)
        num2 = len(xyz2)
        with open(os.path.join(dir, sub_dir1, sub_dir2, f"atom_info"), "w") as f:
            f.write(
                """### Informations about range of atoms in *xyz file
    ### First line  - structer's 1
    ### Second line - structer's 2\n"""
            )
            f.write(sub_dir1 + f"=1-{num1}\n")
            f.write(sub_dir2 + f"={1+num1}-{num1+num2}\n")
        return 1

    darkblue = "#1f538d"
    self.s1.configure(fg_color=darkblue)
    self.s2.configure(fg_color=darkblue)
    self.save_button.configure(state="disabled")

    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis1 = str(self.spinbox_5.get())
    basis2 = str(self.spinbox_6.get())

    dir = filedialog.askdirectory(initialdir=self.__InitPath__)
    path = str()
    for i in self._name["s1"]:
        for j in self._name["s2"]:
            obj1 = Structure1_translate(i)
            xyz_obj1 = obj1.translate_center_to_zero

            obj2 = Structure2_add_rotate(i, j)
            xyz_obj2 = obj2.rotate_object

            name = np.append(obj1.get_name, obj2.get_name)
            chk_name = path.split(".")[0]  # checkpoint name

            xyz_str = np.append(xyz_obj1, xyz_obj2, axis=0).round(decimals=4)

            xyz_str = np.array(
                ["{:.5f}".format(line) for line in xyz_str.flatten()]
            ).reshape(xyz_str.shape)

            sub_dir1 = i.split("/")[-1].replace(".xyz", "")
            if not os.path.isdir(os.path.join(dir, sub_dir1)):
                os.mkdir(os.path.join(dir, sub_dir1))
            sub_dir2 = j.split("/")[-1].replace(".xyz", "")
            if not os.path.isdir(os.path.join(dir, sub_dir1, sub_dir2)):
                os.mkdir(os.path.join(dir, sub_dir1, sub_dir2))

            if "/" in i or j:
                path = j.split("/")[-1].replace(".xyz", "") + "_" + i.split("/")[-1]

            save(xyz_str, name, path)
            atom_info(xyz_obj1, xyz_obj2, sub_dir1, sub_dir2)
            txt = dft_info(
                nproc,
                ram,
                chk_name,
                charge,
                multiplicity,
                basis1,
                basis2,
                self._default_method,
            )
            with open(os.path.join(dir, sub_dir1, sub_dir2, "dft_info"), "w") as f:
                f.write(txt)

    self._name = {}


def optionmenu_callback(self):
    self.select_frame_by_name("DxyzS")


def viewButtonFunc2(self):
    nproc = str(self.spinbox_1.get())
    ram = str(self.spinbox_2.get())
    charge = str(self.spinbox_3.get())
    multiplicity = str(self.spinbox_4.get())
    basis1 = str(self.spinbox_5.get())
    basis2 = str(self.spinbox_6.get())
    txt = dft_info(
        nproc, ram, "<name>", charge, multiplicity, basis1, basis2, self._default_method
    )
    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", txt)
    self.consoletextbox.configure(state="disabled")
    self._consoleText = txt


def edit_method(self, method):
    def save(text, window):
        match method:
            case self._default_method:
                self._default_method = text.get("0.0", "end")
            case _:
                self._default_method_dipole = text.get("0.0", "end")
        window.destroy()

    new = customtkinter.CTkToplevel(self)
    new.geometry("750x250")
    new.title("Method")
    txt = customtkinter.CTkTextbox(new)
    txt.insert("0.0", method)
    txt.pack(fill="both", expand=True)
    button = customtkinter.CTkButton(
        new,
        text="Save & Exit",
        fg_color="green",
        hover_color=("#00b300", "#009900"),
        command=lambda: save(txt, new),
    )
    new.bind("<Escape>", lambda _: save(txt, new))
    button.pack(fill="both", expand=True)


def openToGaussianDir(self):
    self.open_button.configure(fg_color="green")
    path = filedialog.askdirectory(initialdir=self.__InitPath__)
    self.list_of_files_agree = {}
    atom_info = {}
    dft_info = {}
    list_of_files_noxyz = []
    errors = set()

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith(".xyz"):
                relpath = os.path.relpath(dirpath, path)
                self.list_of_files_agree[dirpath] = relpath
                ati = any(
                    [True if i == "atom_info" else False for i in os.listdir(dirpath)]
                )
                dfti = any(
                    [True if i == "dft_info" else False for i in os.listdir(dirpath)]
                )
                if ati == True:
                    atom_info[dirpath] = ("atom_info OK", "agree")
                else:
                    atom_info[dirpath] = ("atom_info ERROR", "error")
                    errors.add(dirpath)

                if dfti == True:
                    dft_info[dirpath] = ("dft_info OK", "agree")
                else:
                    dft_info[dirpath] = ("dft_info ERROR", "error")
                    errors.add(dirpath)
                self.save_button.configure(state="normal")

        for dirname in dirnames:  # There no xyz file check
            absPath = os.sep.join([dirpath, dirname])  # abs dir path
            ld = os.listdir(absPath)
            ans = any([True if i.endswith(".xyz") else False for i in ld])
            if ans == False:
                list_of_files_noxyz.append(os.path.relpath(absPath, path))

    customtkinter.CTkTextbox.tag_config(
        self.consoletextbox, "agree", foreground="green"
    )
    customtkinter.CTkTextbox.tag_config(
        self.consoletextbox, "warning", foreground="#e6ac00"
    )
    customtkinter.CTkTextbox.tag_config(self.consoletextbox, "error", foreground="red")
    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.insert("0.0", self._consoleText)
    self.consoletextbox.insert("end", "\n\n")
    for a, d, direc in zip(
        atom_info.values(),
        dft_info.values(),
        self.list_of_files_agree.values(),
    ):
        self.consoletextbox.insert("end", f"{direc}\t\t\t\t xyz files: OK\n", "agree")
        self.consoletextbox.insert("end", f"\t\t\t\t {a[0]}\n", a[1])
        self.consoletextbox.insert("end", f"\t\t\t\t {d[0]}\n", d[1])
        self.consoletextbox.insert("end", "\n\n", d[1])
    self.consoletextbox.insert("end", "\n")
    for n in list_of_files_noxyz:
        self.consoletextbox.insert("end", f"{n}\t\t\t ALERT: no xyz files\n", "warning")
    self.consoletextbox.configure(state="disabled")

    for key in errors:  # remove from dict directory without atom_info/dft_info
        del self.list_of_files_agree[key]


def gaussianInputCreator(self):
    def block(xyz_coor, atom):
        Q = []
        to_block = xyz_coor[: int(atom.split("-")[1])]
        unlock = xyz_coor[int(atom.split("-")[1]) :]
        for line in to_block:
            spl = line.split()
            Q.append(
                "{}{:>8}{:>12}{:>13}{:>13}\n".format(
                    spl[0], "-1", spl[1], spl[2], spl[3]
                )
            )

        return Q + unlock

    for path in self.list_of_files_agree:
        n1 = path.split("/")[-1]
        n2 = path.split("/")[-2]
        f_xyz = [f for f in os.listdir(path) if f.endswith("xyz")][0]
        with open(path + "/dft_info") as dft, open(path + "/atom_info") as atom, open(
            os.path.join(path, f_xyz)
        ) as xyz:
            atom_info = atom.readlines()
            dft_info = dft.readlines()
            atom_1 = atom_info[3][1 + atom_info[3].index("=") :].replace("\n", "")
            atom_2 = atom_info[4][1 + atom_info[4].index("=") :].replace("\n", "")
            xyz_coor = xyz.readlines()[2:]

            if self._froze.get() == "on":
                xyz_coor = block(xyz_coor, atom_1)

            idx = [i for i, item in enumerate(dft_info) if re.search("--", item)][0]
            up = dft_info[:idx]
            down = dft_info[1 + idx :]

            idx_chk = [i for i, item in enumerate(up) if "%chk" in item][0]
            up[idx_chk] = up[idx_chk].replace("\n", f"{n1}_{n2}\n")
            charge = up[-1][0]

            idx_dft = [i for i, item in enumerate(down) if re.search("^[***]", item)]

        with open(os.path.join(path, f_xyz.replace("xyz", "com")), "w") as com:
            com.write("".join(up))
            com.write("".join(xyz_coor))
            com.write("\n")
            com.write(atom_1 + " " + charge + "\n")
            com.write("".join(down[: idx_dft[1] - 1]))
            com.write(atom_2 + " " + charge + "\n")
            com.write("".join(down[idx_dft[1] - 1 :]))
            com.write("\n\n")
    self.consoletextbox.configure(state="normal")
    self.consoletextbox.delete("0.0", "end")
    self.consoletextbox.configure(state="disabled")

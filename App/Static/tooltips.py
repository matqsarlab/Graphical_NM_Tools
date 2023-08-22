from abc import ABC, abstractmethod

from tktooltip import ToolTip


class My_Tooltip(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def text(self):
        pass

    def tooltip(self, button):
        return ToolTip(button, msg=lambda: self.text(), delay=0.3)


class GeneralButtons(My_Tooltip):
    def __init__(self, button="") -> None:
        super().__init__()
        self.button = button

    def text(self):
        match self.button:
            case "nproc":
                return "Set number of processor for Gaussian input file."
            case "ram":
                return "Set RAM value [GB] for Gaussian input file."
            case "charge":
                return "Set charge of system for Gaussian input file."
            case "multiplicity":
                return "Set multiplicity of system for Gaussian input file."
            case "nrotbonds":
                return "Set a number of rotable bonds in selected structure."
            case "roughness":
                return (
                    "Set a number of chemical groups on surface in selected structure."
                )
            case "natoms":
                return "Set a number of atoms in selected structure."
            case "nlonepair":
                return (
                    "Set a number of lone electronic pair donor in selected structure."
                )
            case "nsp2atoms":
                return "Set a number of sp2 carbon atoms in selected structure."


class BasisSet(My_Tooltip):
    def __init__(self, switcher="com") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "s1":
                return "Set Basis Set for Material in Gaussian input file."
            case "s2":
                return "Set Basis Set for Molecule in Gaussian input file."
            case _:
                return "Set Basis Set for atoms in Gaussian input file."


class Pseudo(My_Tooltip):
    def text(self):
        return (
            "Set Effective Core Potential functional for atoms in Gaussian input file."
        )


class View(My_Tooltip):
    def __init__(self, switcher="material") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "case1":
                return "dipole"
            case "case2":
                return "Update information about selected atoms and surface structure from loaded  Gaussian `*.log` file."
            case _:
                return "Show current settings in Gaussian input file."


class Edit(My_Tooltip):
    def text(self):
        return "Edit methodology by specyfying Route section in Gassuan input file."


class AtomIdx(My_Tooltip):
    def text(self):
        return "Specify atoms and corners (boundary) to calculate surface area."


class Open(My_Tooltip):
    def __init__(self, switcher="xyz") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "log":
                return "Load Gaussian `*.log` files."
            case _:
                return "Load `*.xyz` structure files."


class Save(My_Tooltip):
    def __init__(self, switcher="com") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "com":
                return (
                    "Save `*.com` Gaussian input files from loaded `*.xyz` structures."
                )
            case "descr":
                return "Calc and Save descriptors in `qsarlab.descr` file."
            case _:
                return "Save `*.xyz` files from loaded structures (Material - Molecule/Dipole)."


class Froze(My_Tooltip):
    def __init__(self, option="com") -> None:
        super().__init__()
        self.option = option

    def text(self):
        if self.option == None:
            return "If checked, Material's atoms are locked."
        else:
            return "If checked, atoms are locked."


class Material(My_Tooltip):
    def __init__(self, switcher="material") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "dipole":
                return "Open the file with the coordinates `xyz` for the dipole."
            case "molecule":
                return "Open the file with the coordinates `xyz` for the molecule."
            case _:
                return "Open the file with the coordinates `xyz` for the material."

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


class Ram(My_Tooltip):
    def text(self):
        return "Set RAM value [GB] for Gaussian input file."


class NProc(My_Tooltip):
    def text(self):
        return "Set number of processor for Gaussian input file."


class Charge(My_Tooltip):
    def text(self):
        return "Set charge of system for Gaussian input file."


class Multiplicity(My_Tooltip):
    def text(self):
        return "Set multiplicity of system for Gaussian input file."


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
    def text(self):
        return "Show current settings in Gaussian input file."


class Edit(My_Tooltip):
    def text(self):
        return "Edit methodology by specyfying Route section in Gassuan input file."


class Open(My_Tooltip):
    def text(self):
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
            case _:
                return "Save `*.xyz` files from loaded structures (Material - Molecule/Dipole)."


class Froze(My_Tooltip):
    def text(self):
        return "If checked, atoms/atom from structure 1 are locked."


class Material(My_Tooltip):
    def __init__(self, switcher="material") -> None:
        super().__init__()
        self.switcher = switcher

    def text(self):
        match self.switcher:
            case "dipole":
                return "dipole"
            case "molecule":
                return "molecule"
            case _:
                return "material"

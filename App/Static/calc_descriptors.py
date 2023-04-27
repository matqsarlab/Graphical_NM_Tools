import numpy as np


class Calc:
    def __init__(self, filename, a1, a2, b1, b2):
        self.filename = filename
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2

    @property
    def gen(self):
        with open(self.filename, "r") as f:
            for i in f:
                yield i

    @property
    def find_line(self) -> tuple:
        x = self.gen

        def selector():

            _ = [next(x) for _ in range(1)]

            charges_list = []
            for j in x:

                if "Sum of" in j or "====" in j:
                    break

                charges_list.append(j)
            return charges_list

        mulliken_ = []
        esp_ = []
        nbo_ = []

        for i in x:

            if "Mulliken charges:" in i:
                mulliken_ = selector()
            if "ESP charges:" in i:
                esp_ = selector()
            if "Charge         Core      Valence    Rydberg      Total" in i:
                nbo_ = selector()

        return mulliken_, esp_, nbo_

    @property
    def standard_orientation(self):

        xyz = []
        x = self.gen

        for i in x:
            if "Standard orientation" in i:

                _ = [next(x) for _ in range(4)]

                xyz = []
                for j in x:

                    if "-\n" in j:
                        break

                    xyz.append(j)
        return xyz

    @property
    def charges_table(self):
        def create_table(kind_charge):
            table = []
            for i in kind_charge:
                s = i.split()
                table.append("{:>3}{:>10}{:>13}".format(s[0], s[1], s[2]))
            return table

        mulliken_ = create_table(self.find_line[0])
        esp_ = create_table(self.find_line[1])
        nbo_ = create_table(self.find_line[2])

        return mulliken_, esp_, nbo_

    def selectAtoms(self, list_of_spec_atoms, number, list_of_atoms, split_num=0):
        lista = self.charges_table[number]
        for i in list_of_spec_atoms:
            for j in lista:
                if str(i) == j.split()[split_num]:
                    list_of_atoms.append(j)
        return list_of_atoms

    def arthmetic(self, list_with_atoms):
        result = list(map(lambda x: float(x.split()[-1]), list_with_atoms))
        return np.mean(result) / self.area

    @property
    def area(self):
        xyz = self.standard_orientation

        for i in xyz:
            line = i.split()
            if self.a1.split()[0] == line[0]:
                a1 = line[3:]
                a1 = np.array(a1).astype(float)
            if self.b1.split()[0] == line[0]:
                b1 = line[3:]
                b1 = np.array(b1).astype(float)
            if self.a2.split()[0] == line[0]:
                a2 = line[3:]
                a2 = np.array(a2).astype(float)
            if self.b2.split()[0] == line[0]:
                b2 = line[3:]
                b2 = np.array(b2).astype(float)

        # area = np.linalg.norm(np.subtract(a1, a2)) * np.linalg.norm(np.subtract(b1, b2))
        area = abs(np.linalg.norm(np.cross(np.subtract(a1, a2), np.subtract(b1, b2))))
        return area

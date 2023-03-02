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
    def area(self):
        xyz = self.standard_orientation

        for i in xyz:
            line = i.split()
            if self.a1 == line[0]:
                self.a1 = line[3:]
            if self.b1 == line[0]:
                self.b1 = line[3:]
            if self.a2 == line[0]:
                self.a2 = line[3:]
            if self.b2 == line[0]:
                self.b2 = line[3:]

        a1 = np.array(self.a1).astype(float)
        a2 = np.array(self.a2).astype(float)
        b1 = np.array(self.b1).astype(float)
        b2 = np.array(self.b2).astype(float)
        area = np.linalg.norm(np.subtract(a1, a2)) * np.linalg.norm(np.subtract(b1, b2))
        return area

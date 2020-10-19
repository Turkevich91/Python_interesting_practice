import re


class Nest:
    STRIKER_REPORT_PATH = r"C:\Users\Public\Documents\Striker Systems\FabCAD\SSNest\Jobs061\$tmpout$.sum"

    class Panel:

        def __init__(self):
            self.name = str()
            self.x_length = float()
            self.y_length = float()
            self.quantity = int()

    def __init__(self):
        self.kit_name = str()
        self.material = str()
        self.material_thickness = float()
        self.parts = dict()
        self.layouts = dict()

    def __str__(self):
        if self.kit_name:
            return self.kit_name

    @property
    def parse_striker_report(self):
        f = open(Nest.STRIKER_REPORT_PATH, "r")
        line = f.readline()
        while line:
            # S = line.replace(':', "").split()

            # Nest information
            if 'Kit Name:' in line:
                self.kit_name = line.split()[-1].strip()
                print(f'Kit name:  {self.kit_name}')
                line = f.readline()
                self.material = line.split()[-1].strip()
                line = f.readline()
                self.material_thickness = float(line.split()[-1].strip())
                print(f'Material: {self.material}')
                print("Material Thickness: %.3f" % self.material_thickness)

            if 'Nest System' in line:
                print('Nest System:')

            if '*** PART SUMMARY ***' in line:  # == '\t*** PART SUMMARY ***\n':
                print('@' * 50 + '\n' + '\t' * 5 + 'Part list\n' + '@' * 50)
                f.readline()  # Просто пропускает одну строку бесполезных данных
                line = f.readline()  # начиная с этой строки и дальше данные проверяются и записываются
                while line != '\n':
                    S = line.replace(':', "").split()
                    S[1], S[2], S[3] = float(S[1]), float(S[2]), int(S[3])
                    # self.parts = {S[0]:{"length_x": float(S[1]), "length_y":float(S[2], "qty":int(S[3])}}
                    print(S[0], '\t\t', str(S[1]).ljust(5), '\t\t', str(S[2]).ljust(6), '\t', S[3])
                    line = f.readline()

            if line.startswith('\t*** Layout Number ') & line.endswith(' ***\n'):
                line = f.readline()
                # while line != '\n':
                #     pass

                line = f.readline()
                # while line != '\n':
                #     pass

            line = f.readline()

        f.close()
        return self


nest = Nest()
nest.parse_striker_report

print(nest, 'nest')

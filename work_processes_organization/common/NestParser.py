import json
import re


class Nest:
    STRIKER_REPORT_PATH = r"C:\Users\Public\Documents\Striker Systems\FabCAD\SSNest\Jobs061\$tmpout$.sum"

    def __init__(self):
        self.kit_name = str()
        self.material = str()
        self.material_thickness = float()
        # info
        self.total_scrap = float()
        self.material_utilization = float()
        self.total_nest_scrap = float()
        self.nest_utilization = float()

        self.parts = dict()
        self.material_set = dict()
        self.layouts = dict()

    def total_parts(self):
        parts = int()
        for part in self.parts.values():
            parts += part['qty']
        return parts

    def total_sheets(self):
        sheets = int()
        for part in self.material_set.values():
            sheets += part['Qty']
        return sheets

    def __str__(self):
        if self.kit_name:
            return self.kit_name

    @property
    def parse_striker_report(self):
        try:
            f = open(Nest.STRIKER_REPORT_PATH, "r")
        except FileNotFoundError:
            print('File not found\nPlease, specify correct file path below:', end="\n")
            f_path = input()
            f = open(f_path, "r")

        # start parsing here:
        while line := f.readline():  # walrus operator!

            # Nest information
            if 'Kit Name:' in line:
                self.kit_name = line.split()[-1].strip()
                line = f.readline()
                self.material = line.split()[-1].strip()
                line = f.readline()
                self.material_thickness = float(line.split()[-1].strip())

                # print(f'Kit name:  {self.kit_name}')
                # print(f'Material: {self.material}')
                # print("Material Thickness: %.3f" % self.material_thickness)

            if 'Nest System' in line:
                # print('Nest System:')
                line = f.readline()
                self.total_scrap = float(line.split(':')[1].strip())
                line = f.readline()
                self.material_utilization = line.split(':')[1].strip()
                line = f.readline()
                self.total_nest_scrap = float(line.split(':')[1].strip())
                line = f.readline()
                self.nest_utilization = line.split(':')[1].strip()

            if "Qty	Width	Length	Patterns" in line:
                head = line.split()
                f.readline(1)
                f.readline(1)
                line = f.readline()
                i = 0
                while line != "\n":
                    lp = line.split()
                    i += 1
                    self.material_set[str(i)] = {head[0]: int(lp[0]), head[1]: float(lp[1]), head[2]: float(lp[2]),
                                                 head[3]: int(lp[3])}
                    line = f.readline()

            if '*** PART SUMMARY ***' in line:
                f.readline()  # Просто пропускает одну строку бесполезных данных
                line = f.readline()  # начиная с этой строки и дальше данные проверяются и записываются
                while line != '\n':
                    S = line.replace(':', "").split()

                    self.parts[S[0]] = {'x': float(S[1]), "y": float(S[2]), "qty": int(S[3])}
                    line = f.readline()

            if '*** Layout Number' in line:

                layout_number = int(re.findall(r'(\d+)', line)[0])
                line = f.readline()
                # print(layout_number)
                self.layouts[layout_number] = {}

                while line != '\n':
                    a = line.strip().split(':')
                    # print(a)
                    self.layouts[layout_number][a[0].strip()] = a[1]

                    line = f.readline()
                line = f.readline()

                if 'PartNo' in line:
                    line = f.readline()

                    self.layouts[layout_number]["Parts"] = {}

                    while line != '\n' and line:
                        ls = line.split()
                        self.layouts[layout_number]["Parts"][ls[0]] = {'Blank/Qty': ls[4], "Total/Qty": ls[5]}
                        # print([ls[0]], [ls[4], ls[5]])
                        line = f.readline()

        f.close()
        return self


nest = Nest()
nest.parse_striker_report
print("TOTAL SHEETS: ", nest.total_sheets())
print(json.dumps(nest.__dict__, indent=3))

import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
import os

SCHEDULES = r"\\mcp-fsvs2\Schedules"


def grab_excel(SCHEDULES=SCHEDULES, filename=None):
    if filename:
        pass
    else:
        return os.listdir(SCHEDULES)


for i in [x for x in grab_excel() if os.path.isfile(os.path.join(SCHEDULES, x))]:
    if i.startswith('~$') \
            or i.endswith('.db',) or i.endswith('.tmp'):
        continue
    elif os.path.splitext(i)[1] == '.xlsx':
        print(i)

import pandas as pd
import os
import re
from pathlib import Path

class PandasHandler:

    def __init__(self):
        self.data_list = []


    def read_csv(self, filename, col_list, delimiter):
        regexp = re.compile('[^ ㄱ-ㅣ가-힣]+')

        data = pd.read_csv(os.path.join(os.path.join(Path(__file__).parent.parent, 'data', filename)),
                           delimiter=delimiter,
                           header=0,
                           names=col_list,
                           encoding='utf8'
                           )

        for i in data.index:
            data_map = {}
            for col in col_list:
                data_map[col] = regexp.sub('', data[col][i].strip())

            self.data_list.append(data_map)

        return self.data_list

    def read_xlsx(self, filename, col_list, usecols):
        data = pd.read_excel(os.path.join(os.path.join(Path(__file__).parent.parent, 'data', filename)),
                           header=0,
                           names=col_list,
                           usecols=usecols,
                           encoding='utf8'
                           )

        for i in data.index:
            data_map = {}
            for col in col_list:
                data_map[col] = str(data[col][i]).strip()

            self.data_list.append(data_map)

        return self.data_list

    def write_xlsx(self, filename, dic):

        df = pd.DataFrame(dic)
        writer = pd.ExcelWriter(os.path.join(os.path.join(Path(__file__).parent.parent, 'data', filename + '.xlsx')), engine='openpyxl')
        df.to_excel(writer, 'Sheet1', index=False)
        writer.save()
from utils import read_Excel
from utils.read_Ini import *
from common.common import *
import os
from utils import excel
import json






# file=os.path.join(data_path,excel_data)
# data = read_Excel.ExcelMethod(file, excel_sheet)
# case=data.get_case()
# getname = read_Excel.ExcelVarles.case_name
#
# print(type(getname))
# for bb in case:
#     cc= dict(bb)['是否开启']
#     print(cc)
# print(case)

# cbs = json.dumps(case)
# print(cbs)
# value = case.get('接口地址')
# print(value)
#
# def gerurl():
case_path = os.path.join(data_path, excel_data)
data = read_Excel.ExcelMethod(case_path, excel_sheet)
#     case = dict(data.get_case())
#     bb= case.__contains__('case')
#     # print()
#     return bb
#
# aa=gerurl()
# print(aa)
bb = read_excel(data)
print(bb)
# aa = bb['case']
# aa=bb[0]
# cc=dict(aa)
# print(type(aa))
# for j in bb:
#     cc=dict(j)
#     print(type(cc))
#     dd=cc['case']
#     print(dd)
import pytest
from utils.read_Excel import *
from utils.read_Ini import *
import os
from common.common import *

#
file=os.path.join(data_path,excel_data)
# result = ExcelMethod(file, excel_sheet)
# data = ExcelMethod(file,excel_sheet).get_case()
# print(data)

# ss= [{'是否开启': '是', '用例名称': '/abc', '请求方式': None, '请求地址': 1, '请求数据': None, '预期结果': None}]
@pytest.mark.parametrize("data",ExcelMethod(file,excel_sheet).get_case())
def test_gwyc_api(data):
    case = data[ExcelVarles.case_name]
    # case1 =case
    # bb = data
    print(case)

@pytest.mark.parametrize("name", ["哈利", "赫敏"])
def test_mm(name):
    print(name)
import openpyxl

class ExcelMethod:
    def __init__(self,filepath,sheet):
        self.filepath=filepath
        self.sheet=sheet

    def open_excel(self):#打开文件
        workbook=openpyxl.load_workbook(self.filepath)
        self.workbook=workbook
        return workbook
    def get_sheet(self):#获取表单
        sheet=self.open_excel()[self.sheet]
        return sheet
    def get_case(self):#获取数据
        rows=list(self.get_sheet().rows)
        title = []
        result = []
        for key in rows[0]:  # 获取所有标题
            title.append(key.value)  # 把标题取出来，并存放在title列表中
        for rows in rows[1:]:  # 获取不含标题的所有行的数据
            dic = {}
            for indx, row in enumerate(rows):
                dic[title[indx]] = row.value
            result.append(dic)
        return result
    def get_switch(self):   #获取用例是否启用
        test = self.get_case()
        switch = []
        for key in test:
            value = key['是否开启']
            switch.append(value)
        return switch
    def get_method(self):   #获取请求方式
        test = self.get_case()
        method = []
        for key in test:
            value = key ['请求方式']
            method.append(value)
        return method
    def get_casename(self):  #获取用例名称
        test = self.get_case()
        caseneme = []
        for key in test:
            value = key['用例名称']
            caseneme.append(value)
        return caseneme
    def get_url(self):  #获取请求路径进行凭借
        test = self.get_case()
        new_url = []
        for bb in test:
            aa = dict(bb)['请求地址']
            new_url.append(aa)
        return new_url
    def get_data(self):   #获取请求数据
        test = self.get_case()
        data = []
        for key in test:
            value = key["请求数据"]
            data.append(value)
        return data
    def get_expectedresults(self):   #获取预期结果
        test = self.get_case()
        expectedresults = []
        for key in test:
            value = key['预期结果']
            expectedresults.append(value)
        return expectedresults
    def write_excel(self,row,column,data):#写入数据
        sheet = self.get_sheet()
        sheet.cell(row,column).value=data
        self.excel_save()
        self.excel_close()

    def excel_save(self):#保存excel
        self.workbook.save(self.filepath)

    def excel_close(self):#关闭excel

        self.workbook.close()


class ExcelVarles:
    case_Id="用例Id"
    case_name="用例名称"
    case_url="请求地址"
    case_method="请求方式"
    case_actual_result="实际结果"
    case_data="请求数据"
    case_headers="请求头"
    case_enforcement="执行结果"
    case_isRun="是否开启"
    case_code="状态码"
    case_result="期望结果"


# 获取用例id
def get_case_id():
    return ExcelVarles.case_Id


# 获取用例名称
def get_case_name():
    return ExcelVarles.case_name


# 用例是否执行
def get_case_is_execute():
    return ExcelVarles.case_isRun


# 接口url
def get_case_interface_url():
    return ExcelVarles.case_url


# 用例方法
def get_case_method():
    return ExcelVarles.case_method


# 请求头
def get_case_header():
    return ExcelVarles.case_headers


# 请求参数
def get_case_payload():
    return ExcelVarles.case_data


# 预期结果
def get_case_expected_result():
    return ExcelVarles.case_result


# 实际结果
def get_case_actual_result():
    return ExcelVarles.case_actual_result


# 用例执行结果
def get_case_result():
    return ExcelVarles.case_enforcement


if __name__ == '__main__':
    print(get_case_id())
    print(get_case_is_execute())


# file=os.path.join(data_path,excel_data)
# data = ExcelMethod(file, excel_sheet)
# print(data.get_case())
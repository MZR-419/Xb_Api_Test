import requests


from utils import Method
import json
from utils.read_Excel import *
from utils.read_Ini import *
from utils import encryptJson
from common.common import random_phone
import pytest
from utils.Method import ApiRequest

file=os.path.join(data_path,excel_data)

@pytest.mark.parametrize('data',ExcelMethod(file,excel_sheet).get_case())
def test_gettoken(data,get_token):
    orderno = random_phone()
    #配置文件的IP与Excel文档请求路径进行拼接
    urls = test_url+data[ExcelVarles.case_url]
    #Excel读取出来的请求参数转为字典
    data1 = str(data[ExcelVarles.case_data])
    if '${orderNo}' in data1:
        new_data = json.loads(data1.replace('${orderNo}',orderno))
        print(new_data)
    #前置加密处理
        datas = encryptJson.EncryptJson.encryptJson(passkey,new_data)
    # print(type(datas))

    if data[ExcelVarles.case_method] == 'get':
        r = Method.ApiRequest().run_method(
            method='get',
            url=data[ExcelVarles.case_url],
            data=datas,
            # headers=headers
        )

    elif data[ExcelVarles.case_method] == 'post':
        header = {
            'Authorization': 'Bearer '+ get_token}
        d = ApiRequest()
        r = d.run_method(
            method='post',
            url=urls,
            data=datas,
            header=header
        )
        # try:
        # aa=(json.loads(data[ExcelVarles.case_result])['code']
            # print('测试通过')
        # writeContent(r.json()['data']['access_tonken'])#提取出返回数据中想要的变量写入到文件中供其他接口使用
        print(r)
        # print(header)




if __name__ == '__main__':
    """执行并生成allure测试报告"""
    pytest.main(["-s","-v","--alluredir","./report/result"]) #运行输出并在report/result目录下生成json文件
    # import subprocess #通过标准库中的subprocess包来fork一个子进程，并进行一个外部的程序
    # subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)#读取json文件并生成html报告，
    #                      # --clean若目录存在则先清除
    # subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html',shell=True)#生成一个本地的服务并自动打开html报告

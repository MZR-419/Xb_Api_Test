import allure
from utils import Log
from utils.read_Excel import *
from utils.read_Ini import *
from utils import encryptJson
from utils.assertion import Assertions
import pytest
from utils.Method import ApiRequest
from common.common import random_phone
import json
import os


file=os.path.join(data_path,excel_data)

@pytest.mark.parametrize('data',ExcelMethod(file,excel_sheet).get_case())
def test_single(data,get_token):
    test = Assertions()
    log = Log.MyLog()
    orderno = random_phone()

    #动态定制每个测试用例的title
    allure.dynamic.title(data[ExcelVarles.case_name])
    #配置文件的IP与Excel文档请求路径进行拼接
    urls = test_url+data[ExcelVarles.case_url]
    #Excel读取出来的请求参数转为字典
    data1 = str(data[ExcelVarles.case_data])

    #判断是否存在${orderNo}，存在就调用函数代替，不存在就按照传的请求
    if '${orderNo}' not in data1:
        datas = encryptJson.EncryptJson.encryptJson(passkey,json.loads(data1))

    elif '${orderNo}' in data1:
        new_data = json.loads(data1.replace('${orderNo}',orderno))
    #前置加密处理
        datas = encryptJson.EncryptJson.encryptJson(passkey,new_data)


    if data[ExcelVarles.case_isRun] == '否':
        log.info(f'测试用例-----{data[ExcelVarles.case_name]}-----不需要执行')
        # return print('不执行该用例')

    elif data[ExcelVarles.case_isRun] == '是':
        header = {
            'Authorization': 'Bearer '+ get_token}

        methods = data[ExcelVarles.case_method]
        r = ApiRequest().run_method(
            method = methods,
            url = urls,
            data = datas,
            header= header
        )
        res = json.loads(r)
        log.info(f'请求返回参数---->{r}')
        print(r)
        try:
            assert test.assert_status_code(res['code'],data[ExcelVarles.case_code])
            log.info(f"测试用例-----{data[ExcelVarles.case_name]}-----测试通过")
            if res['code'] != 1000:
                assert test.assert_single_item(res['msg'],data[ExcelVarles.case_result])
                log.info(f"异常流测试用例-----{data[ExcelVarles.case_name]}-----测试通过")
        except AssertionError as e:
            log.error(f"测试用例-----{data[ExcelVarles.case_name]}-----测试失败")
            raise e




if __name__ == '__main__':
    """执行并生成allure测试报告"""
    pytest.main([])
    os.system(r"allure generate allure-results -o allure-report --clean")
    os.system('allure open allure-report')
    # pytest.main(["-s","-v",'--alluredir',"./report"]) #运行输出并在report/result目录下生成json文件
    # split = 'allure ' + 'generate ' + './report ' + '-o ' + './report/html ' + '--clean'
    # os.system(split)
    # """执行并生成allure测试报告"""
    # pytest.main(["-s","-v","--alluredir","./report/result"]) #运行输出并在report/result目录下生成json文件
    # os.system('allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean')
    # import subprocess #通过标准库中的subprocess包来fork一个子进程，并进行一个外部的程序
    # subprocess.call('allure generate ./report/result/ -o report/html --clean',shell=True)#读取json文件并生成html报告，
    #                      # --clean若目录存在则先清除
    # subprocess.call('allure open -h 127.0.0.1 -p 9999 ./report/html',shell=True)#生成一个本地的服务并自动打开html报告
    # pytest.main(['-v', '--html=./report/all_report.html', '--self-contained-html'])
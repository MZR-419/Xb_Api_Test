# coding:utf-8
from utils import encryptJson
import requests
import json
import pytest
from utils.read_Excel import *
from utils.read_Ini import *
import os
import utils.encryptJson
from utils.Method import ApiRequest


# file=os.path.join(data_path,excel_data)
# result = ExcelMethod(file, excel_sheet)
# data = result.get_case()

# @pytest.mark.parametrize('data',data)
# def test_gwyc_api(self,data):
#     case = data[ExcelVarles.case_name]
#     print(case)
# batchNo = {
#     "username": "98769969",
#     "password": "afdd0b4ad2ec172c586e2150770fbf9e",
#     "appVersion": "2.0"
# }
# print(type(batchNo))
# code = "|xwE9UtuA0u=(:UF"
# data=encryptJson.EncryptJson.encryptJson(code, batchNo)
# print(data)
# url="https://stage-new-api.xinshuiguanjia.com/oauth/token"
#
# bb = requests.post(url=url ,data=data, verify=False)
# print(bb.text)

# data = {"username":"38467807","password":"afdd0b4ad2ec172c586e2150770fbf9e","appVersion":"2.0"}
# code ='|xwE9UtuA0u=(:UF'
# aa = encryptJson.EncryptJson.encryptJson(code,data)
# print(type(aa))

from jpype import *
import jpype
# aa = os.path.join(os.path.abspath('.'), "/jmeter_java.jar")
# print(getDefaultJVMPath())

# jarpath1 = os.path.join(os.path.abspath('.'), "../jmeter_java.jar")
# print(getDefaultJVMPath())
# # #启动java环境，-Djava.class.path指定要应用的jar包，将两个包的地址都放在这里，就实现了导入多个jar包的目的
# jpype.startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath1))
# #使用jar包中的类。通过包名.类名。包名为：com.melot.kktv.util.类名为：SecurityFunctions.
# security_class = jpype.JClass("com.example.EncryptUtil")
# #实例化一个对象
# se_instance = security_class()
# batchNo = json.dumps(data)
# up = str(se_instance.encryptJson(code, batchNo))
# jpype.shutdownJVM()
# return up


# #获取jar包的位置
# jarpath1 = os.path.join(os.path.abspath('.'), "../JPypeTest/gson-2.2.4.jar")
# jarpath2 = os.path.join(os.path.abspath('.'), "../JPypeTest/melot-util-1.0.20.jar")
# #打印出jvm的路径
# print(getDefaultJVMPath())
# #启动java环境，-Djava.class.path指定要应用的jar包，将两个包的地址都放在这里，就实现了导入多个jar包的目的
# jpype.startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s;%s" % (jarpath1, jarpath2))
# #使用jar包中的类。通过包名.类名。包名为：com.melot.kktv.util.类名为：SecurityFunctions.
#
# security_class = jpype.JClass("com.melot.kktv.util.SecurityFunctions")
# json_parser_class = jpype.JClass("com.google.gson.JsonParser")
# #实例化一个对象
# se_instance = security_class()
# js_instance = json_parser_class()
# #通过对象调用SecurityFunctions类内的方法，得到加密后的up值
# up = se_instance.upEncode("u=555000031&p=a123456")
# print (up)
# json_str = '{"platform":2,"a":1,"c":12002,"v":1083,"deviceModel":"samsung_SM-G610F","deviceUId":"5408b9b0c73c1b80b0","FuncTag":40000015,"imei":"357488087243412","up":"%s" }' % (up)
# print ((json_str))
# #通过调用JsonParser类里面的方法，将字符串转化成json对象
# jsonEl = js_instance.parse(json_str)
# jsonObj = jsonEl.getAsJsonObject()
# #通过调用SecurityFunctions类内的方法，得到加密后的sv值
# sv = security_class.getSingedValue(jsonObj)
# print (sv)
# #关闭jvm
# jpype.shutdownJVM()


# url = token_url
# print(url)
# data = encryptJson.EncryptJson.encryptJson(passkey, token_data)
# print(data)
# method = 'post'
# # r = ApiRequest()
# # dd = r.run_method(method=method, url=url, data=data, verify=False)
#
# r = requests.post( url = url, data=data,verify=False)
# print(r.text)

# token_url =' https://stage-new.api.xinshuiguanjia.com/oauth/token'
# token_data = {"username":"38467807","password":"afdd0b4ad2ec172c586e2150770fbf9e","appVersion":"2.0"}
#
# data = encryptJson.EncryptJson.encryptJson(passkey,token_data)
#
# r = requests.post(url=token_url, data=data)


d = 'aa:1','bb:2'

bb='bb:2' in d
aa = d
print(bb)
#
# for i in d():
#     # if "2" in i:
#     #     i = i.replace('2','dhhd')
#
#     print(type(i))
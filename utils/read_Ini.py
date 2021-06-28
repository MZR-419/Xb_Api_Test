from configparser import  ConfigParser
from config.config import *
import json
class ReadDataIni(ConfigParser):
    def __init__(self,filename):
        super(ReadDataIni,self).__init__() #继承父类的构造函数
        self.read(filename)

    def read_data_ini(self,section=None,option=None):
        #读取data.ini文件的内容的方法
        value=self.get(section,option) #获取对应节点的值
        return  value


path=os.path.join(path,'Xb_ApiTest.ini') #获取文件的绝对路径
r=ReadDataIni(path)

#获取配置文件中Excel文件名字，与sheets
excel_data=r.read_data_ini('excel_data','name')
excel_sheet = r.read_data_ini('excel_data','sheet')

#获取测试环境的Url
test_url = r.read_data_ini('http_url','url')

#获取密钥
passkey = r.read_data_ini('passkey', 'key')

#token请求地址和参数
token_url = r.read_data_ini('token', 'token_url')
token_data = json.loads(r.read_data_ini('token', 'token_data'))
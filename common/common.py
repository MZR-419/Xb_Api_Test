import pandas as pd
import os
import random

#读取Excel数据方法
def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, **kwargs)
        data_dict = data.to_dict('records')
    finally:
        return data_dict

#获取指定的目录
def fileDir(data):
    """
    :param data: 目录
    :return: 返回
    """
    base_path=os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_path,data)#将获取到的目录返回
#获取路径下的文件，调用需要传递两个参数替换，否则使用默认的参数
def filePath(fileDir="data",fileName="case.xlsx"):
    """
    :param fileDir:目录
    :param fileName: 文件名称
    :return: 返回
    """
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,fileName)

def random_phone():
    '''随机生成手机号'''
    while True:
        phone = '1' + random.choice(['1', '3'])  # 随机以13或15开头的号段
        for i in range(12):
            num = random.randint(0, 9)
            phone += str(num)
        return phone



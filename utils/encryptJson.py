#对数据进行加密方法

import jpype
import os
import json
from jpype._jvmfinder import getDefaultJVMPath


class EncryptJson():
    def encryptJson(code, data):
        # 获取jar包的位置
        jarpath1 = os.path.join(os.path.abspath('.'), "../jmeter_java.jar")
        # #启动java环境，-Djava.class.path指定要应用的jar包，将两个包的地址都放在这里，就实现了导入多个jar包的目的
        try:
            jpype.startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath1),
                     convertStrings=False)
        except:
            pass
        # jpype.startJVM(getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % (jarpath1))
        # #使用jar包中的类。通过包名.类名。包名为：com.melot.kktv.util.类名为：SecurityFunctions.
        security_class = jpype.JClass("com.example.EncryptUtil")
        # #实例化一个对象
        se_instance = security_class()
        batchNo = json.dumps(data)
        up = str(se_instance.encryptJson(code, batchNo))
        # jpype.shutdownJVM()
        return json.loads(up)
        jpype.shutdownJVM()



# batchNo = {
#     "username": "73205972",
#     "password": "afdd0b4ad2ec172c586e2150770fbf9e",
#     "appVersion": "2.0"
# }
# code = "|xwE9UtuA0u=(:UF"
# aa = EncryptJson.encryptJson(code,batchNo)
# print(type(aa))
# url="https://stage-new-api.xinshuiguanjia.com/oauth/token"
#
# bb = requests.post(url=url ,data=data, verify=False)
# print(bb.text)
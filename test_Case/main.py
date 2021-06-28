import pytest
import os
#作者：道长
"""切换环境"""

#使用哪个环境打开哪个环境
#测试环境
# Environ = "/configs/test"
#预发布环境
# Environ = "/configs/uat"

if __name__ == '__main__':
    pytest.main([])
    os.system(r"allure generate allure-results -o allure-report --clean")
    os.system('allure open allure-report')  # 打开报告

#失败重试
# • 测试失败后要重新运行n次，要在重新运行之间添加延迟时 间，间隔n秒再运行。
# • 执行:
# • 安装:pip install pytest-rerunfailures
# • pytest -v - -reruns 5 --reruns-delay 1 —每次等1秒 重试5次

#并发运行
# 前提:用例之间都是独立的，没有先后顺序，随机都能执行，可重复运行不 影响其他用例。
# 安装:Pip3 install pytest-xdist
# • 多个CPU并行执行用例，直接加-n 3是并行数量:pytest -n 3 • 在多个终端下一起执行

    # os.system('--alluredir=allure-results  --clean-alluredir')#清理之前的
    # os.system('allure generate allure-results -o allure-report -c ')#allure generate命令的时候会从这些测试结果集中去生成HTML报告

    # pytest.main(["-sq",
    #              "--alluredir", "./allure-results"])
    # os.system(r"allure generate --clean allure-results -o allure-report")




import pytest
import os

if __name__ == "__main__":
    pytest.main(['test_Case/test_Single.py', '--alluredir', './report'])
    os.system('allure generate ./report -o ./report --clean')
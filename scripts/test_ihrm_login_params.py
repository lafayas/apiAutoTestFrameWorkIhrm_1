import unittest

from parameterized import parameterized
from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from common.read_json_util import read_json_data
from config import BASE_DIR

"""
参数化实现步骤:
1. 导包 from parameterized import parameterized
2. 在通用测试方法上一行, 添加 @parameterized.expand()
3. 给 expand() 传入 [(),(),()] 格式数据。 (调用 read_json_data())
4. 修改 通用测试方法形参, 按 数据中的 key 设计 参数。
5. 在 通用测试方法 内, 使用形参
"""


class TestIhrmLoginParams(unittest.TestCase):
    path_filename = BASE_DIR + "/data/ihrm_login.json"

    # 通用测试方法 (实现参数化)
    @parameterized.expand(read_json_data(path_filename))
    def test_login(self, desc, req_data, status_code, success, code, message):
        # 调用自己封装的接口
        resp = IhrmLoginApi.login(req_data)
        print(desc, ":", resp.json())

        # 断言
        assert_util(self, resp, status_code, success, code, message)

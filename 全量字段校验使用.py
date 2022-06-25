import unittest

import jsonschema

from api.ihrm_login_api import IhrmLoginApi


class TestIhrmLogin(unittest.TestCase):
    # 登录成功
    def test01_login_success(self):
        # 组织请求数据
        json_data = {"mobile": "13800000002", "password": "123456"}

        # 调用自己封装的接口
        resp = IhrmLoginApi.login(json_data)
        print("登录成功:", resp.json())

        # 断言
        # assert_util(self, resp, 200, True, 10000, "操作成功")

        # 断言 校验响应状态码
        self.assertEqual(200, resp.status_code)

        # 使用全量字段校验, 替换 断言
        # 校验规则
        schema = {
            "type": "object",
            "properties": {
                "success": {"const": True},
                "code": {"const": 10000},
                "message": {"pattern": "操作成功"},
                "data": {"type": "string"}
            },
            "required": ["success", "code", "message", "data"]
        }

        # 调用jsonschema校验函数

        jsonschema.validate(instance=resp.json(), schema=schema)

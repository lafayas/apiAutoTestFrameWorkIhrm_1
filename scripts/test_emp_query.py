import logging
import unittest

from api.ihrm_emp_curd import IhrmEmpCURD
from common.db_util import DBUtil
from common.get_header import get_header
from config import BASE_DIR
from logging_use import init_log_config


class TestEmpQuery(unittest.TestCase):
    header = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.header = get_header()

    def setUp(self) -> None:
        insert_sql = "insert into bs_user(id, mobile, username) values('1234567890123', '13998765412', '没有名字');"
        DBUtil.uid_db(insert_sql)

    def tearDown(self) -> None:
        delete_sql = "delete from bs_user where id = '1234567890123';"
        DBUtil.uid_db(delete_sql)

    # 测试 查询员工
    def test01_query_emp(self):
        resp = IhrmEmpCURD.query_emp("1234567890123", self.header)
        print("查询员工:", resp.json())

import requests

# 添加员工
url = "http://ihrm-java.itheima.net/api/sys/user"
header = {"Content-Type": "application/json",
          "Authorization": "Bearer de677c5a-18e7-4d25-87d0-ab87dae4fea6"}
json_data = {
    "username": "业务猪001",
    "mobile": "13978734773",
    "workNumber": "9527"
}
resp = requests.post(url=url, headers=header, json=json_data)
print("添加员工：", resp.json())

# 查询员工
url_query = "http://ihrm-java.itheima.net/api/sys/user/1469566449784717312"
header_query = {"Content-Type": "application/json",
                "Authorization": "Bearer de677c5a-18e7-4d25-87d0-ab87dae4fea6"}
resp_query = requests.get(url=url_query, headers=header_query)
print("查询员工：", resp_query.json())

# 修改员工
url_modify = "http://ihrm-java.itheima.net/api/sys/user/1469566449784717312"
header_modify = {"Content-Type": "application/json",
                 "Authorization": "Bearer de677c5a-18e7-4d25-87d0-ab87dae4fea6"}

modify_data = {"username": "齐天大圣"}
resp_modify = requests.put(url=url_modify, headers=header_modify, json=modify_data)
print("修改员工：", resp_modify.json())

# 删除员工
url_del = "http://ihrm-java.itheima.net/api/sys/user/1469566449784717312"
header_del = {"Authorization": "Bearer de677c5a-18e7-4d25-87d0-ab87dae4fea6"}
resp_del = requests.delete(url=url_del, headers=header_del)
print("删除员工：", resp_del.json())

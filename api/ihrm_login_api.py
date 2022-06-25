import requests


class IhrmLoginApi(object):
    # 登录方法
    @classmethod
    def login(cls, json_data):
        url = "http://ihrm-java.itheima.net/api/sys/login"
        header = {"Content-Type": "application/json"}
        resp = requests.post(url=url, headers=header, json=json_data)
        return resp


if __name__ == '__main__':
    print(IhrmLoginApi.login({"mobile": "13800000002", "password": "123456"}).json())

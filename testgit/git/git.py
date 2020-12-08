import requests


class Demo:
    addUser_url = 'https://zhizi-release.arkfintech.cn/'

    def test(self, url):
        new_url = self.addUser_url + url
        userData = {
            "jsCode": "013FJR4l1hBuzq0ziN4l18KR4l1FJR4g"
        }
        rep = requests.post(new_url, data=userData)
        print(rep.text)
        getaddUser = (rep.json()['sessionKey'])
        print(getaddUser)

        if getaddUser is None:

            print("失败")
        else:

            print("成功")


d = Demo()

d.test('weixin/getSessionKey')

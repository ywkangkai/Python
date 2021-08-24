import requests





#注册
# url = 'http://192.168.254.128:8080/app/mobile/api/user/register'
#
# data = {"mobile":"15680570930","password":"123456","code":"3367","platform":"windows","username":"test11","sex":1,"age":20,"email":"158000000011@test.com"}
#
# header = {
#     "Content-Type": "application/json;charset=utf-8",
#     "Accept": "application/json"
# }
#
# re = requests.post(url,headers=header, json=data)
#
# print(re.text)

#登录

url = 'http://192.168.254.128:8080/app/mobile/api/user/login'

data = {"mobile":"15680570930","password":"123456","gqid":"4000000"}

header = {
    "Content-Type": "application/json;charset=utf-8",
    "Accept": "application/json"
}

re = requests.post(url,headers=header, json=data)

print(re.text)
import http.client
import urllib
import random

from app.extensions import db
from app.models import Users

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C58946984"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "0fc1b6f405f0b3b99f5fcbb5cae7e4d4"

def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def sms(num):
    u = Users.query.filter_by(phone=num).first()
    mobile = num
    num1 = str(random.randint(100000, 999999))
    text = "您的验证码是：" + num1 + "。请不要把验证码泄露给其他人。"
    if not u:
        user = Users(phone=num, phone_num=num1, password=None)
        db.session.add(user)
        send_sms(text, mobile)
        u = Users.query.filter_by(phone=num).first()
    else:
        u.phone_num = num1
        db.session.add(u)
        send_sms(text, mobile)
    return str(u.id)
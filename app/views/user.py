import datetime
import os, re, random

from PIL import Image
from flask import Blueprint, request, current_app, session
from flask.json import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models import Users, Personal
from app.sms import sms


user = Blueprint('user', __name__)


# 登录
@user.route('/login/', methods=['POST','GET'])
def login():
    if not request.json or 'username' not in request.json or 'password' not in request.json:
        return jsonify({'ret': 'true', 'state': 0})  # 格式错误
    data = {
        'username': request.json['username'],
        'password': request.json['password'],
    }
    if re.match(r'1[34578]\d{9}', data['username']) == None:
        u1 = Personal.query.filter_by(nickname=data['username']).first()
        if u1 != None:
            u2 = Users.query.filter_by(id=u1.user_id).first()
            if check_password_hash(u2.password, data['password']) == False:
                return jsonify({'ret': 'true', 'state': 1})  # 密码错误
            p = Personal.query.filter_by(user_id=u2.id).first()
            session['user_id'] = p.id
            # 登录成功返回的数据
            data = {
                'state': 2,
                'icon': p.icon,
                'username': p.nickname,
                'sex': p.sex,
                'address': p.address,
                'birthday': p.birthday,
                'introduce': p.introduce,
                'id': p.id,
            }
            return jsonify({'ret': 'true', 'data': data})  # 登录成功
        else:
            return jsonify({'ret': 'true', 'data': {'state': 3}})  # 账户不存在
    else:
        u = Users.query.filter_by(phone=data['username']).first()
        if u != None:
            if check_password_hash(u.password, data['password']) == False:
                return jsonify({'ret': 'true', 'data': {'state': 1}})  # 密码错误
            p = Personal.query.filter_by(user_id=u.id).first()
            session['user_id'] = p.id
            # 登录成功返回的数据
            data = {
                'state': 2,
                'icon': p.icon,
                'username': p.nickname,
                'sex': p.sex,
                'address': p.address,
                'birthday': p.birthday,
                'introduce': p.introduce,
                'id': p.id
            }
            return jsonify({'ret': 'true', 'data': data})  # 登录成功
        else:
            return jsonify({'ret': 'true', 'data': {'state': 3}})  # 账户不存在


# 退出登录
@user.route('/logout/', methods=['POST','GET'])
def logout():
    session.clear()
    return jsonify({'ret': 'true', 'data': {'start': 1}}) # 操作成功


# 修改密码
@user.route('/mpw/', methods=['POST','GET'])
def mpw():
    if not request.json or 'username' not in request.json or 'password' not in request.json\
            or 'verification' not in request.json:
        return jsonify({'ret': 'true', 'data': {'state': 0}})  # 格式错误
    data = {
        'phone': request.json['username'],
        'phone_num': request.json['verification'],
        'password': request.json['password']
    }
    u = Users.query.filter_by(phone=data['phone']).first()
    if u.phone_num != int(data['phone_num']):
        return jsonify({'ret': 'true', 'data': {'state': 2}})  # 验证码错误
    else:
        u.phone_num = None
        u.password = generate_password_hash(data['password'])
        return jsonify({'ret': 'true', 'data': {'state': 1}})  # 请求成功

# 发送验证码
@user.route('/register/send/sms/', methods=['POST'])
def register_send():
    if not request.json or 'username' not in request.json:
        return jsonify({'ret': 'true', 'data': {'state': 0}})  # 格式错误
    data = {
        'phone': request.json['username']
    }
    sms(data['phone'])
    return jsonify({'ret': 'true', 'data': {'state': 1}})   # 请求成功

# 注册
@user.route('/register/',methods=['POST'])
def register():
    if not request.json or 'username' not in request.json or 'password' not in request.json\
            or 'verification' not in request.json:
        return jsonify({'ret': 'true', 'data': {'state': 0}})  # 格式错误
    data = {
        'phone': request.json['username'],
        'phone_num': request.json['verification'],
        'password': request.json['password']
    }
    u = Users.query.filter_by(phone=data['phone']).first()
    # 判断用户是否注册
    p = Personal.query.filter_by(user_id=u.id).first()
    if p:
        return jsonify({'ret': 'true', 'data': {'state': 4}})  # 用户已经注册

    if u != None:
        phone_num = data['phone_num']
        if int(phone_num) != u.phone_num:
            return jsonify({'ret': 'true', 'data': {'state': 1}})  # 验证码错误返回
        u.password = generate_password_hash(data['password'])
        db.session.add(u)

        # 注册的默认信息
        name = ''
        for i in range(10):
            name += chr(random.randint(97, 122))
        user = Personal(nickname=name,address='北京-海淀',introduce='该用户很懒没有留下任何数据',user_id=u.id, icon=r'\static\upload\default.jpg')
        u.phone_num = None
        db.session.add(user)
        return jsonify({'ret': 'true', 'data': {'state': 2}})  # 注册成功
    return jsonify({'ret': 'true', 'data': {'state': 3}})  # 注册失败


# 修改信息
@user.route('/add/information/', methods=['POST','GET'])
def add_information():
    user = session.get('user_id')
    if user != None:
        data = {
            'icon': request.files.get('icon'),
            'nickname': request.values.get('nickname'),
            'sex': request.values.get('sex'),
            'address': request.values.get('address'),
            'introduce': request.values.get('introduce'),
        }
        p = Personal.query.filter_by(id=user).first()
        if data['nickname'] and Personal.query.filter_by(nickname=data['nickname']).first() == None:
            p.nickname = data['nickname']
        if request.values.get('birthday') and request.values.get('birthday') != 'undefined'\
                and re.match(r'(\d{4}-\d{1,2}-\d{1,2})', request.values.get('birthday')) != None:
            x = datetime.datetime.strptime(request.values.get('birthday'), '%Y-%m-%d')
            p.birthday = x
        if data['sex']:
            p.sex = data['sex']
        if data['address']:
            p.address = data['address']
        if data['introduce']:
            p.introduce = data['introduce']
        if data['icon']:
            p.icon = icon(data['icon'], user)
        db.session.add(p)
        data1 = {
            'state': 1,
            'icon': p.icon,
            'username': p.nickname,
            'sex': p.sex,
            'address': p.address,
            'birthday': p.birthday,
            'introduce': p.introduce,
            'id': p.id
        }
        return jsonify({'ret': 'true', 'data': data1})  # 修改成功
    else:
        return jsonify({'ret': 'true', 'data': {'state': 0}})  # 修改失败


# 头像上传
def icon(img, id):
    # 获取用户的id
    p = Personal.query.filter_by(id=id).first()
    # 获取上传信息
    file = img
    # 生成随机的文件名
    suffix = os.path.splitext(file.filename)[1]
    filename = random_string() + suffix
    # 拼接完成的路径名
    pathname = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'], filename)
    # 删除原来的头像，默认的除外
    if p.icon != r'\static\upload\default.jpg':
        x = str(r'\leju\app'+p.icon)
        os.remove(os.path.abspath(x))
    # 保存上传后的文件
    file.save(pathname)
    # 生成缩略图
    img = Image.open(pathname)
    # 重新设置尺寸
    img.thumbnail((128, 128))
    # 重新保存
    img.save(pathname)
    f1 = os.path.join(r'\static\upload', filename)
    return f1


# 生成字符串
def random_string(length=32):
    import random
    base_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.choice(base_str) for i in range(length))


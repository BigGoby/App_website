import os

base_dir = os.path.abspath(os.path.dirname(__file__))

# 通用配置
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # 数据库自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 警告不显示
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件发送
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or '服务器地址'
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or '账号'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '授权码'

    # 文件上传
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
    UPLOADED_PHOTOS_DEST = os.path.join(base_dir, r'static\upload')

    BABEL_DEFAULT_LOCALE = 'zh_CN'
    # 额外的初始化操作，即使什么内容都没有写，也是有意义的
    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'leju-dev.sqlite')


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'leju-test.sqlite')


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'leju.sqlite')


# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

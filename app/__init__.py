from flask import Flask, render_template
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint

# 封装一个方法，专门用于创建Flask实例
def create_app(config_name): # development
    # 创建应用实例
    app = Flask(__name__)
    # 初始化配置
    app.config.from_object(config.get(config_name) or config['default'])
    # 调用初始化函数
    config[config_name].init_app(app)
    # 配置扩展
    config_extensions(app)
    # 配置蓝本
    config_blueprint(app)
    # 错误页面定制
    config_errorhandler(app)
    # 返回应用实例
    return app


def config_errorhandler(app):
    # 如果在蓝本定制，只针对本蓝本的错误有效，
    # 可以使用app_errorhandler定制全局有效的错误显示
    @app.errorhandler(404)
    def page_not_found(e):
        # return render_template('errors/404.html')
        pass
# 导入类库
from flask_babelex import Babel
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_uploads import UploadSet, IMAGES
from flask.ext.admin import Admin

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
moment = Moment()
migrate = Migrate(db=db)
photos = UploadSet('photos', IMAGES)
admin = Admin()
babel = Babel()

# 初始化
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    babel.init_app(app)

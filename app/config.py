import os
import redis
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    SESSION_TYPE = 'redis' # session类型为redis
    SESSION_FILE_DIR = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    pass

# app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
# app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port='6379', password='123123')  # 用于连接redis的配置
# app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
# app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
# app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上 session:cookie值进行加密
# Session(app)

config = {
    'default': DevelopmentConfig,
}
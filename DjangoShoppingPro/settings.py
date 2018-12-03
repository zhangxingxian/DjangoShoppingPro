import os
import sys

# 根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置全局apps的路径,确保python能搜索的到apps目录, 也可以不配置
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '7t101&gt_*$95vw-^xliuqta1j12g^spxy331#*8*c*&m4=ds)'

DEBUG = True

ALLOWED_HOSTS = []

# 体统App
SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 自定义App
CUSTOM_APPS = [
    'apps.account',
    'apps.detail',
    'apps.search',
    'apps.cate',
    'apps.main',
    'apps.shoppingcart',
    'apps.testdj',
    'apps.order',
]

# 第三方App
EXT_APPS = [
    'xadmin',
    'crispy_forms',
    # 非必要 主要用于修改样式
    'reversion',
    'django_ajax',
]

INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS + EXT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoShoppingPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'apps/account/templates'),
            os.path.join(BASE_DIR, 'apps/cate/templates'),
            os.path.join(BASE_DIR, 'apps/detail/templates'),
            os.path.join(BASE_DIR, 'apps/main/templates'),
            os.path.join(BASE_DIR, 'apps/search/templates'),
            os.path.join(BASE_DIR, 'apps/testdj/templates'),
            os.path.join(BASE_DIR, 'apps/order/templates'),
        ]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoShoppingPro.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': 'sunck',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 语言设置
LANGUAGE_CODE = 'zh-hans'
# 时区设置
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 时候开启django时区
USE_TZ = False

# 访问静态文件的路径配置
STATIC_URL = '/static/'

# ============配置静态文件整理的根目录==========
# 最后整合和collectstatic命令有关
STATIC_ROOT = 'static_root'
# ===========end配置静态文件整理的根目录========

# 配置静态文件的位置
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/main/static'),
    os.path.join(BASE_DIR, 'apps/detail/static'),
    os.path.join(BASE_DIR, 'apps/shoppingcart/static'),
    os.path.join(BASE_DIR, 'apps/testdj/static'),
    os.path.join(BASE_DIR, 'apps/order/static'),
)

# 如果user表继承了auth的user表就得配置AUTH_USER_MODEL
AUTH_USER_MODEL = 'main.User'

# 定义全局的登陆跳转url
LOGIN_URL = '/account/login/'

# ===============配置访问多媒体的路径=============
MEDIA_URL = '/media/'
# 配置文件上传的目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# ===============end配置访问多媒体的路径==========

# ===============发送邮箱配置==========
# 发送邮件的服务器地址
EMAIL_HOST = 'smtp.163.com'
# 发送邮件端口
EMAIL_PORT = 25
# 发送邮件默认的名称
EMAIL_HOST_USER = 'zhangxx_xy@163.com'
# 授权码
EMAIL_HOST_PASSWORD = 'zhang895'
# 是否启用tls安全协议
EMAIL_USE_TLS = True

# 是否启用SSL安全协议
# EMAIL_USE_SSL = True
# 发送超时时间
# EMAIL_TIMEOUT =
# ===============发送邮箱配置 end ==========


# =========================缓存的配置=====================
# pip install django-redis
CACHES = {
    "default": {
        # 使用redis做缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        # 缓存的地址
        'LOCATION': 'redis://127.0.0.1:6379/1',
        # rediss: //[:password]@localhost:6379 / 0
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据
            # "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
    'session': {
        # 指定缓存的类型是文件缓存
        'BACKEND': 'django_redis.cache.RedisCache',
        # 将缓存的数据保存在该目录下
        'LOCATION': 'redis://127.0.0.1:6379/15',
        'TIMEOUT': 300,
        'OPTIONS': {
            # "PASSWORD": ""
            # 是否压缩缓存数据(非必要)
            "COMPRESSOR": "django_redis.compressors.lzma.LzmaCompressor",
            # 配置连接池
            "CONNECTION_POOL_KWARGS": {"max_connections": 100, "retry_on_timeout": True}
        }
    },
}

# session使用redis座位缓存
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"
# session失效的时间 7天
SESSION_COOKIE_AGE = 7 * 24 * 60 * 60  # Session的cookie默认失效日期（2周） 默认1209600秒
# =====================缓存配置end=====================

# =======日志配置=======
LOGGING = {

}

# ======================支付宝支付相关配置==================
APP_ID = ''


# ======================END支付宝支付相关配置==================

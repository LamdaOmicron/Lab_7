# authapp/oauth_config.py

import os
from dotenv import load_dotenv

load_dotenv()

class YandexOAuthConfig:
    """Конфигурация OAuth для Яндекс"""

    CLIENT_ID = os.getenv('YANDEX_CLIENT_ID')
    CLIENT_SECRET = os.getenv('YANDEX_CLIENT_SECRET')
    REDIRECT_URI = os.getenv('YANDEX_REDIRECT_URI', 'http://localhost:4200/auth/oauth/yandex/callback')
    
    AUTHORIZATION_URL = 'https://oauth.yandex.ru/authorize'
    TOKEN_URL = 'https://oauth.yandex.ru/token'
    USER_INFO_URL = 'https://login.yandex.ru/info'
    
    SCOPE = 'login:email login:info'  # Запрашиваемые права
    STATE_EXPIRES_IN = 300  # 5 минут для state-токена
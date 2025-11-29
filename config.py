import os
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') or os.getenv('DISCORD_BOT_TOKEN')
FIREBASE_URL = os.getenv('FIREBASE_URL')
FIREBASE_SECRET = os.getenv('FIREBASE_SECRET')
FIREBASE_SERVICE_ACCOUNT = os.getenv('FIREBASE_SERVICE_ACCOUNT')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_MODEL = os.getenv('DEEPSEEK_MODEL','deepseek-chat')
DEEPSEEK_BASE = os.getenv('DEEPSEEK_BASE','https://api.deepseek.com/v1')
BOT_OWNER_ID = os.getenv('BOT_OWNER_ID')
ADMIN_USER_IDS = [x.strip() for x in os.getenv('ADMIN_USER_IDS','').split(',') if x.strip()]
PORT = int(os.getenv('PORT','8000'))
RATE_LIMIT_USER = int(os.getenv('RATE_LIMIT_USER','10'))

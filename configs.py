import json
import os


#def load_token(file_path='token.json'):
#    with open(file_path, 'r') as file:
#        token = json.load(file)
#    return token.get('token')

TELEGRAM_BOT_KEY  = "399367993:AAGcDodVySFJ4Mk32bTciuvkamrD-8ns0ow"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE = os.path.join(BASE_DIR, "SplitMoneyBot/logs/logs.log")
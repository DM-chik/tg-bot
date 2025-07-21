import aiogram
from dotenv import load_dotenv
import os
load_dotenv()
bot_token = os.getenv('TOKEN')
print(bot_token)
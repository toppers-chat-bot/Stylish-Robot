import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "7919953730:AAHWnnboW1GrdAkdZlTKaPX7TKWpsSPyovY")
      API_ID = int(os.environ.get("API_ID", "22182189"))
      API_HASH = os.environ.get("API_HASH", "5e7c4088f8e23d0ab61e29ae11960bf5")
      OWNER_ID = int(os.environ.get("OWNER_ID", "8181241262"))


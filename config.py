import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7911253896:AAFLtGAbVIo6yJPC9biHjMvpKgQwEwwVTag")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27628439"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "f9e19f1a0e6d4f81fe35b55502ef6669")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", " 1695549408"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "kzltelebot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

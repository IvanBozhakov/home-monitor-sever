# home-monitor-sever
# Installation 
```pip install -r requirements.txt```

# Config
Rename .env.local to .env and fill credentials
```
# Api client token
API_BEARER_TOKEN=

# Telegram 
TELEGRAM_API_TOKEN=
TELEGRAM_CHAT_ID=

# Database
DATABASE=
```

# Run 
```uvicorn main:app --reload```

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "11472991"))
    API_HASH = getenv("API_HASH", "c78c50d54baf2173e8b3f75c359c0c72")
    BOT_TOKEN = getenv("BOT_TOKEN", "7815292408:AAGWF66HeTOnuK_JNgkii5DrOpQS75SN2do")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002450932371")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1430742022").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://KarthikMovies:KarthikUK007@cluster0.4l5byki.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

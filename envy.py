import os

os.environ.setdefault("MONGO_URI", "mongodb+srv://root:r00tUser@myfirstcluster-hmnju.mongodb.net/cocktail_mix?retryWrites=true&w=majority")
os.environ.setdefault("SECRET_KEY", "randomstring123")
os.environ.setdefault("MONGO_DBNAME", "cocktail_mix")
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
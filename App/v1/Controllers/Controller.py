from App.v1.Providers.database import db, Base


class Controller:
    def __init__(self):
        self.db = db()
        self.Base = Base
    def __del__(self):
        self.db.close()
    
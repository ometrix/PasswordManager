import datetime

class Entry:
    def __init__ (self, plataform, user, password, position=None, date_created=None, date_updated=None):
        self.plataform = plataform
        self.user = user
        self.password = password
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()

    def __repr__ (self) -> str:
        return f"({self.plataform},{self.user}, {self.password}, {self.position}, {self.date_created}, {self.date_updated})"

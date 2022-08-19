from typing import List
import datetime
from password_manager.model import Entry
from password_manager import db, EntryQuery

def create(entry: Entry) -> None:
    entry.position = len(db)+1
    new_entry = {
        'plataform': entry.plataform,
        'user' : entry.user,
        'password': entry.password,
        'position': entry.position,
        'date_created': entry.date_created,
        'date_updated': entry.date_updated,
    }
    db.insert(new_entry)

def read() -> List[Entry]:
    results = db.all()
    entrys = []
    for result in results:
        new_entry = Entry(result['plataform'], result['user'], result['password'], result['position'], result['date_created'], result['date_updated'])
        entrys.append(new_entry)
    return entrys
 
def update(position: int, plataform: str, user: str, password: str) -> None:
    if plataform is not None and user is not None and password is not None :
        db.update({'plataform': plataform, 'user': user, 'password': password}, EntryQuery.position == position)

    elif plataform is not None and password is not None :
        db.update({'plataform': plataform, 'password': password}, EntryQuery.position == position)

    elif plataform is not None :
        db.update({'plataform': plataform}, EntryQuery.position == position)

    elif user is not None and password is not None :
        db.update({'user': user, 'password': password}, EntryQuery.position == position)

    elif user is not None :
        db.update({'user': user}, EntryQuery.position == position)

    elif password is not None:
        db.update({'password': password}, EntryQuery.position == position)    

def delete(position) -> None:
    count = len(db)
    db.remove(EntryQuery.position == position)
    for pos in range(position+1, count):
        change_position(pos, pos-1)

def change_position(old_position: int, new_position: int) -> None:
    db.update({'position': new_position}, EntryQuery.position == old_position)
    

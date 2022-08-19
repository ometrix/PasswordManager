from tinydb import TinyDB, Query

db = TinyDB('password-manager.json')
db.default_table_name = 'password-manager'
EntryQuery = Query()
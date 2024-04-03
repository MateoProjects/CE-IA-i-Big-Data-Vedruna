import sqlite3

PATH_DB = "C:\\Users\\rmate\\Desktop\\sqlite-tools-win-x64-3450200\\test_db.db"
# Creo la conexio amb la BD
con = sqlite3.connect(PATH_DB)
cur = con.cursor()

def select_all():
    resultat = cur.execute("SELECT * FROM persona")
    res = resultat.fetchall()
    return res



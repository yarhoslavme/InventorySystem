import sqlite3
from sqlite3 import Error
from werkzeug import security


def sql_connection():
    try:
        con = sqlite3.connect('systemdb.db')
        return con;
    except Error:
        print(Error)


def init_db():
    print("Init DB")
    strsql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        username    TEXT,
        password    TEXT,
        email   TEXT,
        rol TEXT
    );
    CREATE TABLE IF NOT EXISTS productos (
        ref TEXT,
        nombre  TEXT,
        precio  REAL,
        cantidad    INTEGER,
        imagen  TEXT
    );
    """

    #Crear la Base de Datos si no existe
    con = sql_connection()
    cursor = con.cursor()
    cursor.executescript(strsql)
    con.commit()

    #Crear usuario administrador si no existe
    strsql = "SELECT * FROM usuarios WHERE username = 'admin'"
    cursor.execute(strsql)
    usuario = cursor.fetchone()
    if usuario is None:
        password_hash = security.generate_password_hash("123456")
        strsql = "INSERT INTO usuarios VALUES ('admin','" + password_hash + "', 'admin@system.com', 'admin')"
        cursor.execute(strsql)
        con.commit()

    con.close()

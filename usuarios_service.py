import sqlite3
from sqlite3 import Error
from systemdb import sql_connection


def listar_usuarios():
    strsql = "SELECT * FROM usuarios;"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql)
    usuarios = cursor.fetchall()
    con.close()
    return usuarios


def usuario_by_username(username):
    strsql = "SELECT * FROM usuarios WHERE username = ?"
    con = sql_connection()
    cursor = con.cursor()
    cursor.execute(strsql, [username])
    usuario = cursor.fetchone()
    con.close()
    return usuario


def agregar_usuario(username, password, email, rol):
    strsql = "INSERT INTO usuarios VALUES (?, ?, ?, ?)"
    con = sql_connection()
    cursor = con.cursor()
    password_hash = security.generate_password_hash(password)
    cursor.execute(strsql, (username, password_hash, email, rol))
    cursor.commit()
    con.close()


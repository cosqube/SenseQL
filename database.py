import sqlite3

from config import DB_PATH


def get_connection():
	connection = sqlite3.connect(DB_PATH)
	connection.row_factory = sqlite3.Row
	connection.execute("PRAGMA foreign_keys = ON")
	return connection


def close_connection(connection):
	if connection is not None:
		connection.close()

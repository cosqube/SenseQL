import pandas as pd

from database import close_connection, get_connection


def _friendly_sqlite_error(error):
	message = str(error)
	lower_message = message.lower()

	if "no such table" in lower_message:
		return f"❌ SQL Execution Error:\n{message}"
	if "no such column" in lower_message:
		return f"❌ SQL Execution Error:\n{message}"
	if "syntax error" in lower_message:
		return f"❌ SQL Execution Error:\n{message}"

	return f"❌ SQL Execution Error:\n{message}"


def run_query(sql):
	connection = None
	try:
		connection = get_connection()
		frame = pd.read_sql_query(sql, connection)
		return frame
	except Exception as error:
		error_frame = pd.DataFrame()
		error_frame.attrs["error"] = _friendly_sqlite_error(error)
		return error_frame
	finally:
		close_connection(connection)

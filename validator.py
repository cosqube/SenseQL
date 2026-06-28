import re


ALLOWED_STARTS = ("SELECT", "WITH")
BLOCKED_KEYWORDS = (
	"DROP",
	"DELETE",
	"UPDATE",
	"INSERT",
	"ALTER",
	"TRUNCATE",
)


def _strip_sql_comments(sql):
	lines = []
	for line in sql.splitlines():
		stripped = line.strip()
		if stripped.startswith("--"):
			continue
		lines.append(line)
	return "\n".join(lines).strip()


def validate_sql(sql):
	if not sql or not sql.strip():
		return False, "❌ Unsafe query: empty SQL"

	cleaned_sql = _strip_sql_comments(sql)
	first_statement = cleaned_sql.split(";")[0].strip()
	if not first_statement:
		return False, "❌ Unsafe query: empty SQL"

	start_keyword = first_statement.lstrip().split(None, 1)[0].upper()
	if start_keyword not in ALLOWED_STARTS:
		return False, f"❌ Unsafe query: only SELECT and WITH statements are allowed (got {start_keyword})"

	if ";" in cleaned_sql.rstrip(";"):
		return False, "❌ Unsafe query: multiple SQL statements are not allowed"

	upper_sql = cleaned_sql.upper()
	for keyword in BLOCKED_KEYWORDS:
		if re.search(rf"\b{keyword}\b", upper_sql):
			return False, f"❌ Unsafe query: blocked keyword detected ({keyword})"

	return True, ""

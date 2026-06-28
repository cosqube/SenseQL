def build_prompt(question, schema):
	return f"""You are an SQLite expert.

Database schema:
{schema}

Rules:
- Return only SQL.
- Do not explain.
- Do not use Markdown.
- Use SQLite syntax.
- If the question cannot be answered using the schema, say so instead of inventing tables.

Question:
{question}
"""

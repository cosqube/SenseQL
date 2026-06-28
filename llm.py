import argparse
import re

from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL, SCHEMA_PATH
from prompt import build_prompt


def load_schema():
	with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
		return file.read()


def clean_sql(text):
	cleaned = text.strip()
	cleaned = re.sub(r"^```(?:sql)?\s*", "", cleaned, flags=re.IGNORECASE)
	cleaned = re.sub(r"\s*```$", "", cleaned)
	return cleaned.strip()


def generate_sql(question):
	if not GROQ_API_KEY:
		raise ValueError("GROQ_API_KEY is not set in .env")

	schema = load_schema()
	prompt = build_prompt(question, schema)

	client = Groq(api_key=GROQ_API_KEY)
	response = client.chat.completions.create(
		model=GROQ_MODEL,
		messages=[
			{"role": "system", "content": "You are an SQLite expert. Return only SQL."},
			{"role": "user", "content": prompt},
		],
		temperature=0,
	)

	content = response.choices[0].message.content or ""
	return clean_sql(content)


def main():
	parser = argparse.ArgumentParser(description="Generate SQL from an English question using Groq.")
	parser.add_argument("question", help="English question to convert into SQL")
	args = parser.parse_args()

	print(generate_sql(args.question))


if __name__ == "__main__":
	main()

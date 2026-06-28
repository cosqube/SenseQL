from execute import run_query
from llm import generate_sql


def run_question(question):
    print(f"Question: {question}")
    sql = generate_sql(question)
    print("Generated SQL:")
    print(sql)
    print()

    results = run_query(sql)
    error_message = results.attrs.get("error")

    if error_message:
        print(error_message)
    elif results.empty:
        print("No results returned.")
    else:
        print("Results:")
        print(results.to_string(index=False))

    print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    questions = [
        "Show all customers",
        "Show top 5 customers by total spending",
        "List all products in Electronics",
        "Show total revenue by category",
    ]

    for question in questions:
        run_question(question)
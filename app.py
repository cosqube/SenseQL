import streamlit as st

from execute import run_query
from llm import generate_sql
from validator import validate_sql


st.set_page_config(page_title="SenseQL", page_icon="🧠", layout="wide")

st.markdown(
	"""
	<div style="text-align:center; padding: 1rem 0 0.5rem 0;">
		<h1>🧠 SenseQL</h1>
		<p style="font-size: 1.1rem; color: #6b7280;">Natural Language → SQL Assistant</p>
	</div>
	""",
	unsafe_allow_html=True,
)

if "history" not in st.session_state:
	st.session_state.history = []

if "question" not in st.session_state:
	st.session_state.question = ""


def set_question(question):
	st.session_state.question = question
	st.session_state.question_input = question


st.sidebar.header("History")
if st.session_state.history:
	for item in st.session_state.history[-10:][::-1]:
		st.sidebar.button(item, key=f"history_{item}", on_click=set_question, args=(item,))
else:
	st.sidebar.caption("Your recent questions will appear here.")

question = st.text_input(
	"Question",
	placeholder="Show the top 5 customers by total spending",
	key="question_input",
)

generate_clicked = st.button("Generate Query", type="primary")

if generate_clicked and question.strip():
	st.session_state.question = question.strip()
	if question.strip() not in st.session_state.history:
		st.session_state.history.append(question.strip())

	try:
		generated_sql = generate_sql(question.strip())
		st.subheader("Generated SQL")
		st.code(generated_sql, language="sql")

		is_valid, validation_message = validate_sql(generated_sql)
		if not is_valid:
			st.error(validation_message)
		else:
			results = run_query(generated_sql)
			error_message = results.attrs.get("error")

			st.subheader("Results")
			if error_message:
				st.error(error_message)
			elif results.empty:
				st.info("No results returned.")
			else:
				st.dataframe(results, use_container_width=True)
				csv_data = results.to_csv(index=False).encode("utf-8")
				st.download_button(
					label="⬇ Download Results",
					data=csv_data,
					file_name="senseql_results.csv",
					mime="text/csv",
				)
	except Exception as error:
		st.error(str(error))


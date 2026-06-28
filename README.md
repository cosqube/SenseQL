# SenseQL

SenseQL is a Streamlit app that converts natural language questions into SQL, validates the query, executes it on SQLite, and shows the results in a table.

## Features

- Natural language to SQL generation with Groq
- SQL safety validation before execution
- SQLite query execution with Pandas DataFrames
- Query history in the sidebar
- CSV export for results

## Setup

1. Install dependencies:

	```powershell
	c:/Users/DELL/Documents/SenseQL/venv/Scripts/python.exe -m pip install -r requirements.txt
	```

2. Add your Groq key to `.env`:

	```env
	GROQ_API_KEY=your_key_here
	```

3. Run the app:

	```powershell
	c:/Users/DELL/Documents/SenseQL/venv/Scripts/python.exe -m streamlit run app.py
	```

## Project Flow

User question → Generate SQL → Validate SQL → Execute SQL → Display results

## Database

The app uses SQLite database file `database/company.db`.

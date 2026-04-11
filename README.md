\# Google ADK Project – Time + Calculator Agent


This project is a custom AI agent built using \*\*Google ADK\*\*, with two tools:

\- A Time Tool (returns system time for any city)

\- A Calculator Tool (add, sub, mul, div)



The agent can be run:

\- In the \*\*ADK Web UI\*\* using `adk web`

\- In the \*\*command line\*\* using `python chat.py`



---



\## 🚀 Features

\- Gemini-powered agent

\- Two custom tools (Time + Calculator)

\- Web interface

\- CMD interface

\- Organized Python package structure



---



\## 📂 Project Structure

google-adk-project/

│

├── README.md

├── requirements.txt

├── .env (not in GitHub, contains API key)

│

├── time\_agent/

│ ├── agent.py

│ ├── chat.py

│ ├── init.py

│ └── .env

│

└── .venv/ (ignored)

---



\## ▶️ Running the Web UI

adk web



Then open:





http://127.0.0.1:8000





---



\## ▶️ Running the CMD Chat



---



\## 🔧 Tools Implemented



\### ⏰ 1. `get\_current\_time(city)`

Returns local system time in a formatted way.



\### 🧮 2. `simple\_calculator(a, b, operation)`

Supports:

\- add

\- sub

\- mul

\- div



---



\## 🔑 API Key Setup

Create a `.env` file in both:

\- `google-adk-project/`

\- `google-adk-project/time\_agent/`



Add:

GOOGLE\_GENAI\_API\_KEY=your\_api\_key\_here





---



\## 👤 Author

Rachana 

⚠️ Note: API keys are stored securely using .env and are not included in this repository.
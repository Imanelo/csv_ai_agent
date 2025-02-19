# CSV AI Analyst

An AI-powered CSV analysis tool that understands natural language queries, built with Python, LangChain, and OpenRouter.


## Features
- Natural language query processing
- OpenRouter AI integration (supports multiple LLMs)
- Data analysis and visualization suggestions
- Dual interface (CLI + GUI)
- Secure code execution sandbox

## Installation

1. **Clone repository**
```sh
git clone https://github.com/YOUR_USERNAME/csv-ai-agent.git
cd csv-ai-agent
```

2. **Install Dependencies**

```sh
pip install -r requirements.txt
echo "OPENROUTER_API_KEY=your_api_key_here" > .env
```


## Usage
**Command Line Interface (CLI)**
```sh
python -m app.main
```
**Graphical User Interface (GUI)**
```sh
python -m app.gui
```
**Example Queries**

"Show average salary by department"

"Who has the highest experience?"

"List employees under 30 in Marketing"

"What's the correlation between age and salary?"

## Configuration
- Edit .env file:

OPENROUTER_API_KEY=your_api_key_here

- Modify config/settings.py to:

- Change default AI model

- Adjust temperature (creativity)

- Customize headers
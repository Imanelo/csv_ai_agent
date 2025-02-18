from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from config.settings import settings

class CSVAIAgent:
    def __init__(self, file_path):
        """Initialize the AI agent with CSV file path"""
        self.file_path = file_path
        self.agent = self._initialize_agent()
        
    def _initialize_agent(self):
        """Create LangChain CSV agent with OpenRouter configuration"""
        return create_csv_agent(
            ChatOpenAI(
                model=settings.OPENROUTER_MODEL,
                openai_api_key=settings.OPENROUTER_API_KEY,
                openai_api_base=settings.OPENROUTER_BASE_URL,
                temperature=0.3,
                default_headers={  # Changed from model_kwargs
                    "HTTP-Referer": "http://localhost:8000",
                    "X-Title": "CSV AI Agent"
                }
            ),
            self.file_path,
            verbose=True,
            allow_dangerous_code=True  # Security acknowledgement
        )
    
    def query(self, question):
        """Process natural language query"""
        try:
            return self.agent.run(question)
        except Exception as e:
            return f"Error processing query: {str(e)}"
    
    def validate_csv(self):
        """Basic CSV validation"""
        try:
            pd.read_csv(self.file_path)
            return True
        except Exception as e:
            return False
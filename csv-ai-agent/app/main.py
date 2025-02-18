from app.agent import CSVAIAgent

def main():
    file_path = input("Enter path to CSV file: ")
    
    try:
        agent = CSVAIAgent(file_path)
        print("CSV file loaded successfully!\n")
        
        while True:
            query = input("\nEnter your question (or 'exit' to quit): ")
            if query.lower() == 'exit':
                break
                
            response = agent.query(query)
            print("\nAnalysis Result:")
            print(response)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
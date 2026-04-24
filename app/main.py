from app.llm import ask_llm
from app.parser import parse_response
from utils.retry import retry
from utils.logger import log
import json

def main():
    while True:
        user_input = input("\nAsk any question: ")

        #Type exit to quit the program
        if user_input.lower() == "exit":
            break

        raw = retry(lambda user_input=user_input: ask_llm(user_input)) #Using lambda to pass user_input to retry
        #parameter user_input with value user_input from the outer scope, ensuring the correct value is used when ask_llm is called within retry
        log("Raw LLM Response:\n" + raw)
        parsed = parse_response(raw)
        log("Parsed Response:\n" + json.dumps(parsed, indent=2)) #Converting parsed dict back to JSON string for better logging

        print("\nAnswer:", parsed["answer"])
        print("Reasoning:", parsed["reasoning"])
        print("Confidence:", parsed["confidence"])  

if __name__ == "__main__":
    main()
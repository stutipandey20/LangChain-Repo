
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set.")

# 1. Setting up the chat prompt template
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

# 2. Define the chat prompt template
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

# 3. Fill the template and get the answer
# question = "Why is the sky blue?"

# # 4. Invoke the LLM with the filled prompt
# prompt = chat_prompt.format_messages(question=question)
# response = llm.invoke(prompt)

# # 5. Print the result
# print("Q:", question)
# print("A:", response.content)

while True:
    question = input("\nAsk me anything (or type 'exit' to quit): ")
    if question.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    # 4. Fill the template and get the response
    prompt = chat_prompt.format_messages(question=question)
    response = llm.invoke(prompt)

    # 5. Print the result
    print("Q:", question)
    print("A:", response.content)
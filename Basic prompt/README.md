
# Basic Prompt Chat with LangChain + Google Gemini (Free)
A simple Python script to interact with Google’s Gemini model using LangChain and a structured prompt template.
Perfect for beginners to understand the flow of LangChain without spending money on API calls.

# Features
Uses Google Gemini (free tier available via Google AI Studio)
Structured prompt with ChatPromptTemplate
Interactive Q&A loop in the terminal
Easy .env setup for API keys

# 1. Get Your Free Gemini API Key
Go to Google AI Studio and log in with your Google account.
Click your profile picture → API keys.
Click Create API key → In new project.
Copy the API key.

# 2. Clone the Repo
git clone <url>
cd <path>

# 3. Install Dependencies
pip install langchain-google-genai python-dotenv

# 4. Set Up Environment Variables
Create a .env file in the project folder:
GOOGLE_API_KEY=your_gemini_api_key_here

# 5. Run the Script
python basic_prompt_chat.py

# 6. Example
Ask me anything (or type 'exit' to quit): What is the capital of California?
Q: What is the capital of California?
A: The capital of California is Sacramento.

Ask me anything (or type 'exit' to quit): quit
Exiting the chat. Goodbye!
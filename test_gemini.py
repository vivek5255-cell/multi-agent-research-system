from google import genai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Send a test request
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Say Hello in one sentence."
)

print(response.text)
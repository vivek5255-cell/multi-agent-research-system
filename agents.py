import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

# Load .env file
load_dotenv()
print("GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)


# -----------------------------
# Search Agent
# -----------------------------
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )


# -----------------------------
# Reader Agent
# -----------------------------
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


# -----------------------------
# Writer Chain
# -----------------------------
writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert research writer. Write clear, structured and insightful reports."
        ),
        (
            "human",
            """
Write a detailed research report on the topic below.

Topic:
{topic}

Research:
{research}

Write a professional report with the following sections:

1. Introduction

2. Key Findings
   - At least 3 detailed findings

3. Conclusion

4. Sources
   - List every URL used
"""
        ),
    ]
)

writer_chain = writer_prompt | llm | StrOutputParser()


# -----------------------------
# Critic Chain
# -----------------------------
critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a strict research reviewer."
        ),
        (
            "human",
            """
Review the report below.

{report}

Return ONLY in this format:

Score: X/10

Strengths:
- ...
- ...

Weaknesses:
- ...
- ...

Suggestions:
- ...
- ...

Final Verdict:
...
"""
        ),
    ]
)

critic_chain = critic_prompt | llm | StrOutputParser()
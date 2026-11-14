from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # reads .env and sets OPENAI_API_KEY in the environment

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

prompt = (
    "Give me exactly 5 healthy breakfast ideas. "
    "Healthy means high in protein or fibre, low in added sugar, and not deep fried. "
    "Format: a numbered list from 1 to 5, one idea per line, "
    "no introduction and no closing remarks."
)

reply = llm.invoke(prompt)
print(reply.content)
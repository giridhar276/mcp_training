

import os 
from langchain_openai import ChatOpenAI
os.environ["OPENAI_API_KEY"] = "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"


llm = ChatOpenAI(model = "gpt-4.1-mini")

response = llm.invoke("what is todays date")

print(response.content)
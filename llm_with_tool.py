



import os 
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from datetime import datetime
os.environ["OPENAI_API_KEY"] = "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"



@tool
def get_date() -> str:
    """return todays date"""
    return datetime.now().strftime("%Y-%m-%d")


tools = [get_date]


llm = ChatOpenAI(model = "gpt-4.1-mini")

llm_with_tools = llm.bind_tools(tools)



response = llm_with_tools.invoke("what is todays date")
print(response)
print(response.content)
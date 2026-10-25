import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
load_dotenv()










model = ChatGroq(
    model_name="qwen/qwen3.8-27b",
    temperature=0,
   #max_tokens=500

)


memory=[SystemMessage(content="You are a Funny Ai Aget.")]

while True:

    user = input("You:")
    memory.append(HumanMessage(content=user))
    if user == "0":
        break

    response = model.invoke(memory)
    memory.append(AIMessage(content=response.content))
    print(f"Bot:{response.content}")



print(memory)

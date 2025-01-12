from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import chainlit as cl

# load the env
load_dotenv()

# @cl.langchain_factory(use_async=True)

# Instantiate the model
model = ChatOpenAI(model="gpt-3.5-turbo")

chat_history = [] # use a list to store the chat history

# set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assitant.")
chat_history.append(system_message)

messages = [
    {"role": "system", "content": "You are a helpful AI assitant."}
]

# chat loop
# while True:
#     query = input("You: ")
#     if query.lower() =='exit':
#         break
query="Hi"
chat_history.append(HumanMessage(content=query))

# Get AI response using history
result = model.invoke(chat_history)
response = result.content
chat_history.append(AIMessage(content=response))
    # print("AI: ",response)


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()

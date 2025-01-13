from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import chainlit as cl

# load the env
load_dotenv()

# @cl.langchain_factory(use_async=True)

# Instantiate the model
client = OpenAI()

from openai import OpenAI
client = OpenAI()

messages=[{"role": "system", "content": "You are a helpful assistant."},]

def chat(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return completion.choices[0].message.content

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content})
    response = chat(messages)
    messages.append({"role": "assistant", "content": response})
    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_openai import OpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
import chainlit as cl
import hashlib  # For password hashing

# Load environment variables
load_dotenv()

# Firebase Firestore setup
PROJECT_ID = "chat-4ff6e"
USER_COLLECTION = "users"  # Collection for storing user credentials
COLLECTION_NAME = "chat_history"

# Initialize Firestore client
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Authentication Callback for Chainlit
@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch user data from Firestore
    user_ref = client.collection(USER_COLLECTION).document(username)
    user_data = user_ref.get()
    
    if user_data.exists:
        stored_password = user_data.to_dict()["password"]
        if stored_password == hash_password(password):
            return cl.User(identifier=username, metadata={"role": "user"})
        else:
            return None  # Invalid password
    else:
        # If user doesn't exist, automatically sign them up (optional)
        hashed_password = hash_password(password)
        user_ref.set({"password": hashed_password})
        return cl.User(identifier=username, metadata={"role": "new_user"})

# Chat handler for Chainlit
@cl.on_chat_start
def on_chat_start():
    # Retrieve the authenticated user from the session
    user = cl.user_session.get("user")
    if user:
        cl.user_session.set("messages", [
            {"role": "system", "content": "You are a helpful assistant."}
        ])
        print(f"User {user.identifier} logged in.")
    else:
        print("User session not found.")

@cl.on_message
async def on_message(message: cl.Message):
    user = cl.user_session.get("user")
    if not user:
        await cl.Message(content="Please log in to continue.").send()
        return

    # Fetch the user's session ID for chat history
    session_id = f"{user.identifier}_session"

    # Initialize chat history in Firestore
    chat_history_ref = client.collection(COLLECTION_NAME).document(session_id)
    chat_history_data = chat_history_ref.get().to_dict() or {"messages": []}
    messages = chat_history_data["messages"]

    # Add user message to chat history
    messages.append({"role": "user", "content": message.content})

    # Generate response from OpenAI
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    response = completion.choices[0].message.content

    # Add assistant message to chat history
    messages.append({"role": "assistant", "content": response})

    # Update chat history in Firestore
    chat_history_ref.set({"messages": messages})

    # Send response back to the user
    await cl.Message(content=response).send()

# 🤖 Chatbot with User Authentication and Firestore Integration 🚀

Welcome to the **AI-Powered Chatbot** project! This chatbot leverages OpenAI's GPT model to provide intelligent conversations, while also integrating **user authentication** and **session-based chat history storage** using **Chainlit** and **Google Firestore**. Built for scalability and modern user interaction, this project demonstrates proficiency in AI, cloud integration, and full-stack development. 🎯

---

## 🌟 Features

✨ **AI-Powered Conversations**  
Powered by OpenAI's `gpt-3.5-turbo`, delivering contextual and meaningful responses.

🔒 **User Authentication**  
Secure user login and signup integrated directly into the Chainlit web interface. Supports session-based chat for unique user interactions.

💾 **Chat History Persistence**  
Seamlessly stores user-chat histories in **Google Firestore** for retrieval and analysis.

⚡ **Scalable and Flexible Design**  
Built with modular architecture using Python, Chainlit, and Firebase, making it easy to extend features or deploy to production.

📋 **Real-World Use Cases**  
- Personal assistants  
- Customer support bots  
- Educational tools  

---

## 🛠️ Tech Stack

| **Technology**      | **Description**                                    |
|----------------------|----------------------------------------------------|
| 🧠 **OpenAI GPT**    | For natural language understanding and generation. |
| 🌐 **Chainlit**      | Web-based conversational interface.                |
| ☁️ **Google Firestore** | Cloud-hosted NoSQL database for chat history.   |
| 🐍 **Python**        | Backend scripting and logic.                       |

---

## 🚀 Installation & Setup

### Prerequisites
1. Python 3.9+ 🐍
2. Firebase Project with Firestore enabled ☁️
3. OpenAI API key 🔑

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables: Create a .env file in the root directory and add:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/firebase-service-account.json
   PROJECT_ID=your_firebase_project_id
   ```
4. Run the app:
   ```bash
   chainlit run app.py -w
   ```
5. Open Chatbot in your browser at:
   ```bash
      http://localhost:8000 🌟
   ```



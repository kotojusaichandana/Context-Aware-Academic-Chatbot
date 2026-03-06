🤖 Context-Aware Academic Chatbot

An intelligent academic chatbot built using Python and Streamlit that can understand user questions using intent detection and respond with relevant information while remembering the conversation context.

This project demonstrates basic Natural Language Processing concepts, context management, and an interactive chatbot interface.

🚀 Features

✅ Context-aware conversation handling
✅ Keyword-based intent recognition
✅ Clean and interactive UI built with Streamlit
✅ Maintains conversation history
✅ Handles unknown queries intelligently
✅ Lightweight and easy to run

🧠 How It Works

The chatbot processes user input and determines the intent using predefined keywords stored in intents.py.

Workflow:

User enters a message.

Text is cleaned using utility functions.

Keywords are matched with predefined intents.

Context manager stores the last conversation intent.

The chatbot returns the appropriate response.

This makes the chatbot context-aware, allowing it to guide users even when their input is unclear.

🛠️ Technologies Used

Python

Streamlit

Basic NLP (Keyword Matching)

Context Management Logic

📁 Project Structure
Context_Aware_Chatbot/
│
├── app.py
├── chatbot_engine.py
├── context_manager.py
├── intents.py
├── utils.py
├── main.py
│
├── README.md
│
├── screenshots/
│   ├── chatbot_ui.png
│   ├── conversation_demo.png
│
└── demo_video.mp4
⚙️ Installation

Clone the repository

github link: https://github.com/kotojusaichandana/Context-Aware-Academic-Chatbot

Navigate to the project folder

cd Context-Aware-Academic-Chatbot

Install dependencies

pip install streamlit
▶️ Running the Application

Run the following command:

streamlit run app.py

Then open the browser at:

 http://localhost:8501
💬 Example Questions

You can try asking:

Hi
What is a chatbot?
Tell me about internships
What is the future scope?
Bye
📸 Demo

The repository includes:

Demo screenshots of the chatbot interface

Conversation examples

A demo video showing the chatbot in action

🎯 Learning Objectives

This project was developed as part of an AI/ML Engineering Internship Learning Task to demonstrate:

Understanding of chatbot architecture

Intent recognition techniques

Context handling in conversational systems

Building interactive AI applications using Python

👩‍💻 Developer

Developed by:
Kotoju Sai Chandana

Computer Science Engineering Student
Passionate about Artificial Intelligence, Machine Learning, and Intelligent Systems

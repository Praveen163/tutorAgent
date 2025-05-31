# AI Tutor Chat

AI Tutor Chat is a web-based application that provides students with interactive help for math and physics questions. It features an AI-powered tutor agent that leverages specialized tools to solve problems and explain concepts step-by-step. The project includes a modern chat interface and a Flask backend.

## Features
- **Conversational AI Tutor:** Answers math and physics questions interactively.
- **Step-by-step Explanations:** Uses dedicated tools for math and physics to show all work and reasoning.
- **Modern UI:** Responsive chat interface with light/dark mode, built using Tailwind CSS.
- **Persistent Chat History:** Maintains conversation context for more natural interactions.

## Project Structure
```
project-root/
│
├── server/
│   ├── server.py     # Main Flask app
│   └── src/
│       ├── app.py    # Tutor agent logic
│       ├── agenticTools.py, geminiModel.py, ...
|
|
│   static/           # Frontend (HTML/CSS/JS)
│       └── index.html
|
|
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <project-root>/server
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Start the Flask server:**
   ```bash
   python server.py
   ```
2. **Access the app:**
   Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Usage
- Type your math or physics question in the chat box.
- The AI tutor will respond with a detailed, step-by-step answer.
- You can reset the chat or toggle between light and dark mode.

## How It Works
- The backend uses a custom agent (see `src/server/src/app.py`) that routes questions to specialized tools for math and physics.
- The frontend (in `src/static/index.html`) provides a chat interface and communicates with the backend via a `/chat` API endpoint.

## Customization
- To add more tools or subjects, extend the agent logic in `src/server/src/app.py` and add new tools in `src/server/src/agenticTools.py`.
- UI customization can be done in `src/static/index.html` using Tailwind CSS.

## License
This project is for educational purposes.

---
Crafted with ❤️ by Praveen 
# Math Problem Solver & Data Search Assistant 🧮

A powerful Streamlit application that combines mathematical problem-solving capabilities with data search functionality using Groq LLM and LangChain.

## Features

- 🔢 Solves complex mathematical problems
- 🔍 Searches Wikipedia for relevant information
- 💡 Provides detailed step-by-step explanations
- 🤖 Uses advanced LLM for reasoning and problem-solving
- 📝 Interactive chat interface
- 🎨 Clean and user-friendly UI

## Prerequisites

- Python 3.8+
- Groq API key

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/your-repo/math-gpt.git
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```bash
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Enter your mathematical question in the text area

4. Click the "Solve Problem" button to get a detailed solution

## How It Works

The application uses three main components:

1. **Wikipedia Tool**: Searches Wikipedia for relevant information about topics mentioned in the question

2. **Calculator Tool**: Handles mathematical expressions and calculations

3. **Reasoning Tool**: Provides logical explanations and step-by-step solutions

The application combines these tools using LangChain's agent framework to:
- Parse user questions
- Determine the best tool for solving each part of the problem
- Generate comprehensive, well-explained solutions

## Technologies Used

- Streamlit: Web interface
- LangChain: Agent and chain management
- Groq: Large Language Model
- Python: Core programming language
- Wikipedia API: Information retrieval

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

![image](https://github.com/user-attachments/assets/d8c19906-bab3-4073-b713-dcc0e705d0fe)
![image](https://github.com/user-attachments/assets/6cabc4eb-a1f1-46c7-a94f-42b681aab74e)



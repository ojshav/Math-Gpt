import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables
load_dotenv()

# Enhanced UI configuration
st.set_page_config(
    page_title="Math Problem Solver & Data Search Assistant",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Improved styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4053;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Advanced Math Problem Solver")
st.markdown("---")

# Get API key from environment variable
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("⚠️ GROQ API Key not found in environment variables. Please set GROQ_API_KEY in your .env file.")
    st.stop()

llm = ChatGroq(model="llama-3.1-70b-versatile", groq_api_key=groq_api_key)

## Initializing the tools
wikipedia_wrapper=WikipediaAPIWrapper()
wikipedia_tool=Tool(
    name="Wikipedia",
    func=wikipedia_wrapper.run,
    description="A tool for searching the Internet to find the vatious information on the topics mentioned"

)

## Initializa the MAth tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tools for answering math related questions. Only input mathematical expression need to bed provided"
)

prompt="""
Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

## Combine all the tools into chain
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Reasoning tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## initialize the agents

assistant_agent=initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a MAth chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# Enhanced UI for question input
st.markdown("### 📝 Enter Your Math Question")
question = st.text_area(
    label="Enter your math question here",
    label_visibility="collapsed",
    placeholder="Example: What is the sum of 25 and 75?",
    height=100,
    key="question_input"
)

# Styled button
if st.button("🔍 Solve Problem", type="primary"):
    if question.strip():
        with st.spinner("🤔 Thinking..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)
            
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Enhanced response display
            st.markdown("### 🎯 Solution:")
            st.markdown(f"""
                <div style='
                    background-color: #f0f8ff; 
                    padding: 20px; 
                    border-radius: 10px;
                    color: #1e1e1e;  # Added dark text color
                    font-size: 16px;  # Added font size
                    line-height: 1.5;  # Added line height for better readability
                '>
                    {response}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a question first!")










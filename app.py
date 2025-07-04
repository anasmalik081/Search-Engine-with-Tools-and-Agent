import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from tools.arxiv_tool import ArxivTool
from tools.wikipedia_tool import WikipediaTool
from tools.duckduckgo_tool import DuckDuckGoTool

# Load Environment Variables
load_dotenv()

# Title
st.title("🔍 LangChain - Chat with search")
"""
In this example, we are using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
"""

# Sidebar settings
st.sidebar.title("Settings")
API_KEY = st.sidebar.text_input("Enter your GROQ API Key: ", type="password")

if "messages" not in st.session_state:
    st.session_state['messages'] = [
        {
            "role": "assistant",
            "content": "Hi, I am a Chatbot who can search the web. How can I help you?"
        }
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Prompt
if prompt:=st.chat_input(placeholder="Hey what is machine learning?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Model
    os.environ["GROQ_API_KEY"] = API_KEY
    model = ChatGroq(model_name="gemma2-9b-it", streaming=True)

    # Tools
    tools = [
        ArxivTool().call_tool(),
        WikipediaTool().call_tool(),
        DuckDuckGoTool().call_tool()
    ]

    # Agent
    agent = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)
    
    with st.chat_message("assistant"):
        call_backs = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = agent.run(st.session_state.messages, callbacks=[call_backs])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
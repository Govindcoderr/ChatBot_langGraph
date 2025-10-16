# App.py

from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END
from typing import TypedDict

# ---- 1. Define the state schema ----
class ChatState(TypedDict):
    input: str
    output: str

# ---- 2. Define the chatbot node ----
def chatbot_node(state: ChatState):
    user_input = state["input"]
    llm = ChatOllama(model="llama3.2:1b")  # or use ChatOllama(model="llama3")
    response = llm.invoke(user_input)
    return {"output": response.content}

# ---- 3. Create the graph with schema ----
graph = StateGraph(ChatState)

# ---- 4. Add the node ----
graph.add_node("chatbot", chatbot_node)

# ---- 5. Define entry and exit ----
graph.set_entry_point("chatbot")
graph.add_edge("chatbot", END)

# ---- 6. Compile the app ----
app = graph.compile()

# ---- 7. Run the chatbot ----
if __name__ == "__main__":
    print("🤖 Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_text = input("You: ")
        if user_text.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        result = app.invoke({"input": user_text})
        print("Bot:", result["output"])
        print()



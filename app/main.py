from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI
from langchain_core.messages.ai import AIMessage
from pydantic import BaseModel
from deepagents import create_deep_agent
import logging

from app.core.config import get_settings

settings = get_settings()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = FastAPI(title=settings.app_title)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello from earthquake-multiagent!"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# llm = ChatOpenAI(
#     model=settings.openai_model,
#     api_key=settings.openai_api_key,
#     base_url=settings.openai_api_base
#     # temperature=settings.openai_temperature,
#     # max_tokens=settings.openai_max_tokens,
# )

llm = ChatOpenAI(
        model="qwen3-14b-claude-4.5-opus-high-reasoning-distill", 
        temperature=0.9,
        # base_url="https://api.openai.com/v1",
        base_url="http://127.0.0.1:1234/v1",
        api_key="empty",  # Set to empty string since the local server does not require an API key
        stream_usage=True
    )

agent = create_deep_agent(
    model=llm,
    system_prompt="You are a helpful assistant",
    tools=[],
    subagents=[]
    # backend=None
)

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


# @app.post("/chat", response_model=ChatResponse)
@app.post("/chat")
def chat(request: ChatRequest):
    # messages = [
    #     ("human", "I love programming."),
    # ]

    messages = {"messages": [{"role": "user", "content": "who are you?"}]} 
    # ai_msg = llm.invoke(messages)
    ai_msg = agent.invoke(messages)

    print(ai_msg)

    # print(resp)
    print(type(ai_msg))
    # response = await llm.ainvoke(request.message)
    return ChatResponse(reply="This is a placeholder response. The actual response from the LLM will be here.")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
    )

# -*- coding: utf-8 -*-
import typing as ty  # noqa: F401

from pydantic import BaseModel
from fastapi.routing import APIRouter
from fastapi.responses import StreamingResponse

from app.providers.llm import llm_chat_provider

router = APIRouter()


class ChatRequest(BaseModel):
    question: str

@router.post(
    "/llm-chat",
    summary="Chat with the LLM model",
)
async def llm_chat_endpoint(request: ChatRequest) -> StreamingResponse:
    """LLM chat endpoint."""
    user_question = request.question

    async def event_generator():
        async for chunk in llm_chat_provider.chat(question=user_question):
            yield f"data: {chunk}\n\n"  # SSE 格式


    # Here you would integrate with your LLM model to get a response
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"  # 告诉浏览器这是事件流
    )

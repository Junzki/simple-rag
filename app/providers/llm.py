# -*- coding: utf-8 -*-
import typing as ty  # noqa: F401

from app.persistence.vectors import storage
from app.language_models.moonshot import MoonshotLanguageModel


class LLMChatProvider(object):

    def __init__(self):
        self.llm = MoonshotLanguageModel(
            retriever=storage.as_retriever(5)
        )

    async def chat(self, question: str) -> ty.AsyncGenerator[str, None]:
        """Asynchronous generator for streaming LLM chat responses."""
        async for chunk in self.llm.stream_generate_text(question):
            yield chunk


llm_chat_provider = LLMChatProvider()

# -*- coding: utf-8 -*-
import typing as ty

import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents.base import Document
from app.core import settings, templates


class MoonshotLanguageModel(object):
    """
    Wrapper for Moonshot LLM via LangChain ChatOpenAI interface.
    """

    LLM_BASE_URL = 'https://api.moonshot.cn/v1'
    LLM_MODEL = 'kimi-k2-turbo-preview'

    TEMPLATE_NAME = 'prompts/context-driven-generic-template.md'

    def __init__(
        self,
        retriever: ty.Callable[..., ty.List[Document]],
        temperature: float = 0.7,
        max_retries: int = 3,
    ):
        self.llm = ChatOpenAI(base_url=settings.llm_base_url or self.LLM_BASE_URL,
                              model=settings.llm_model or self.LLM_MODEL,
                              api_key=settings.llm_token,
                              temperature=temperature,
                              max_retries=max_retries,
                              streaming=True)

        self.retriever = retriever

        self.prompt = ChatPromptTemplate.from_template(templates.load_template(self.TEMPLATE_NAME))

        self.rag_chain = (
                {"context": self.retriever | self.format_docs, "question": RunnablePassthrough()}
                | self.prompt
                | self.llm
                | StrOutputParser()
        )


    @staticmethod
    def format_docs(docs: ty.List[Document]):
        return "\n\n".join([d.page_content for d in docs])

    def generate_text(
        self,
        question: str,
    ) -> str:
        response = self.rag_chain.invoke(question)
        return response

    async def stream_generate_text(
        self,
        question: str,
    ):
        async for chunk in self.rag_chain.astream(question):
            yield chunk

        await asyncio.sleep(0)  # Ensure generator is async

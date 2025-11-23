# -*- coding: utf-8 -*-
"""Core application components."""
from .template_loader import TemplateLoader
from .config import settings

settings = settings
templates = TemplateLoader()


class SimpleRAG(object):
    """A simple Retrieval-Augmented Generation (RAG) system."""

    def __init__(self):
        self.settings = settings
        self.templates = templates
        self.storage = None  # Placeholder for storage component
        self.language_model = None  # Placeholder for language model component

    def init(self):
        from app.persistence.vectors import storage
        from app.language_models.moonshot import MoonshotLanguageModel

        self.storage = storage
        self.language_model = MoonshotLanguageModel(
            retriever=self.storage.as_retriever(5)
        )


rag = SimpleRAG()

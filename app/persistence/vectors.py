# -*- coding: utf-8 -*-
import os.path
import typing as ty

import torch
from langchain_chroma.vectorstores import Chroma
from langchain_core.documents.base import Document
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

from app.core.config import settings


class VectorStorage(object):
    """Wrapper for BGE embeddings."""
    DEFAULT_MODEL_NAME = "BAAI/bge-m3"
    DEFAULT_TOP_K = 3

    @property
    def mps_available(self):
        return torch.backends.mps.is_available() and torch.backends.mps.is_built()

    def get_device(self):
        if torch.cuda.is_available():
            return "cuda"
        elif self.mps_available:
            return "mps"
        else:
            return "cpu"

    def __init__(self, model_name: str = DEFAULT_MODEL_NAME,
                 data_storage_path: str = ""):
        self.model_name = model_name

        model_kwargs = {"device": self.get_device()}
        encode_kwargs = {'normalize_embeddings': True}

        self.embeddings = HuggingFaceBgeEmbeddings(model_name=model_name,
                                                   model_kwargs=model_kwargs,
                                                   encode_kwargs=encode_kwargs)

        self._storage = str(settings.data_storage_path)
        if not os.path.exists(self._storage):
            os.makedirs(self._storage, exist_ok=True)
        elif not os.path.isdir(self._storage):
            raise ValueError(f"Data storage path {self._storage} is not a directory.")

        self._db = Chroma(
            embedding_function=self.embeddings,
            persist_directory=self._storage
        )

    def add_documents(self, docs: ty.List[Document]):
        """Load a document into the vector storage."""
        self._db.add_documents(docs)

    def query(self, needle: str, top_k: int = DEFAULT_TOP_K) -> ty.List[Document]:
        """Query the vector storage."""
        results = self._db.similarity_search(needle, k=top_k)
        return results

    def as_retriever(self, top_k: int = DEFAULT_TOP_K):
        """Get a retriever interface for the vector storage."""
        return self._db.as_retriever(search_type="similarity", search_kwargs={"k": top_k})


storage = VectorStorage()

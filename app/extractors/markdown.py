# -*- coding: utf-8 -*-
import pathlib
import typing as ty  # noqa: F401

from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter


class MarkdownExtractor(object):

    HEADERS_TO_SPLIT_ON = [
        ("#", 'Header_1'),
        ("##", 'Header_2'),
        ("###", 'Header_3'),
        ("####", 'Header_4'),
        ("#####", 'Header_5'),
        ("######", 'Header_6'),
    ]

    def split_markdown_file(self, file_path: str | pathlib.Path,
                            encoding: str = None) -> ty.List[ty.Any]:
        """Read a Markdown file and split its content into smaller chunks."""
        with open(file_path, 'r', encoding=encoding or 'utf-8') as f:
            markdown_text = f.read()

        return self.split_markdown(markdown_text)

    def split_markdown(self, markdown_text: str) -> ty.List[ty.Any]:
        """Split Markdown text into smaller chunks based on headers and character limits."""
        header_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=self.HEADERS_TO_SPLIT_ON,
            strip_headers=True,
        )

        # First split by headers
        header_splits = header_splitter.split_text(markdown_text)

        # Further split by character limits
        char_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", "", "。", "？", "！"]
        )

        final_splits = char_splitter.split_documents(header_splits)

        return final_splits

import os
import re

from dotenv import load_dotenv
from backend.config import get_model
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)

import google.generativeai as genai

load_dotenv()

_embeddings = None


def get_embeddings():
    global _embeddings

    if _embeddings is None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        genai.configure(
            api_key=api_key
        )

        _embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001"
        )

    return _embeddings


def split_resume(
    resume_text
):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    return splitter.split_text(
        resume_text
    )


def create_vector_store(
    chunks
):

    db = FAISS.from_texts(
        texts=chunks,
        embedding=get_embeddings()
    )

    db.save_local(
        "vector_store"
    )

    return db


def load_vector_store():

    return FAISS.load_local(
        "vector_store",
        get_embeddings(),
        allow_dangerous_deserialization=True
    )


def build_resume_context(
    question,
    resume_text,
    max_chars=6000
):

    chunks = split_resume(
        resume_text
    )

    question_terms = set(
        re.findall(
            r"\w+",
            question.lower()
        )
    )

    ranked_chunks = sorted(
        chunks,
        key=lambda chunk: len(
            question_terms.intersection(
                re.findall(
                    r"\w+",
                    chunk.lower()
                )
            )
        ),
        reverse=True
    )

    context = "\n\n".join(
        ranked_chunks[:4]
        or chunks[:4]
    )

    return context[:max_chars]


def ask_resume_question(
    question,
    resume_text=None
):

    if resume_text:
        context = build_resume_context(
            question,
            resume_text
        )

    else:
        db = load_vector_store()

        docs = db.similarity_search(
            question,
            k=4
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

    prompt = f"""
    Answer ONLY using the resume information.

    Resume Context:
    {context}

    Question:
    {question}
    """

    response = get_model().generate_content(
        prompt
    )

    return response.text

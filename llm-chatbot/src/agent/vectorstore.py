"""Builds a vectorstore from a webpage."""
import bs4

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from .config import settings


def build_vectorstore(url: str, persist_dir: str = "data/embeddings"):
    """
        Loads a webpage, splits it into chunks, embeds them, and stores them in a vectorstore.

    Args:
        url (str): Webpage source to embed.
        persist_dir (str): Directory to optionally save embeddings.

    Returns:
        InMemoryVectorStore: The constructed vectorstore containing embedded chunks.
    """

    # 1. Load webpage
    bs4_strainer = bs4.SoupStrainer(
        class_=("post-title", "post-header", "post-content")
    )  # only keep post titiles and content

    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs={"parse_only": bs4_strainer},
    )

    docs = loader.load()

    if not docs:
        raise ValueError("Failed to load webpage — no documents returned.")

    print(f"Loaded {len(docs)} documents.")

    # 2. Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # chunk size (characters)
        chunk_overlap=200,  # chunk overlap (characters)
        add_start_index=True,  # track index in original document
    )
    all_splits = text_splitter.split_documents(docs)

    # 3. Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL)

    # 4. Create vectorstore
    vector_store = InMemoryVectorStore(embeddings)
    document_ids = vector_store.add_documents(documents=all_splits)
    print(f"Created vectorstore with {len(document_ids)} documents.")

    return vector_store


# Lazy-loaded singleton vectorstore
_vectorstore = None


def get_vectorstore():
    """
    Returns the application-wide vectorstore instance.
    Builds it on first use.
    """
    global _vectorstore

    if _vectorstore is None:
        _vectorstore = build_vectorstore(
            url=settings.DOC_URL,
            persist_dir=settings.VECTORSTORE_DIR,
        )

    return _vectorstore

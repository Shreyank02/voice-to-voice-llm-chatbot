import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA

def load_document(file_path: str, file_type: str):
    if file_type == "pdf":
        loader = PyPDFLoader(file_path)
    elif file_type == "txt":
        loader = TextLoader(file_path)
    elif file_type == "docx":
        loader = Docx2txtLoader(file_path)
    else:
        raise ValueError("Unsupported file type")
    return loader.load()

def build_rag_chain(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(docs)

    embedding = OllamaEmbeddings(model="llama3.2-vision:11b", base_url="http://91.107.230.57:11434/")
    vectordb = Chroma.from_documents(chunks, embedding)

    llm = ChatOllama(model="llama3.2-vision:11b", base_url="http://91.107.230.57:11434/")
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return rag_chain

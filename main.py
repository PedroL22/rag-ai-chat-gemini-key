import os
import sys

from dotenv import load_dotenv
from llama_index.core import (
    Settings,
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.llms.google_genai import GoogleGenAI

load_dotenv()

# Configuration
DOCUMENTS_FOLDER = "transcripts"
INDEX_STORAGE_PATH = "./storage_gemini"
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "gemini-2.5-pro"

# API Key validation
if not GOOGLE_API_KEY:
    print("Error: Google API key not found.")
    print("Please create a .env file and add the line: GOOGLE_API_KEY='your_key_here'")
    sys.exit(1)

print("Starting RAG AI Chat with Gemini API...")

# Configure Gemini models
llm = GoogleGenAI(model_name=MODEL_NAME, api_key=GOOGLE_API_KEY)
embed_model = GoogleGenAIEmbedding(
    model_name="models/embedding-001", api_key=GOOGLE_API_KEY
)

Settings.llm = llm
Settings.embed_model = embed_model

# Check if index already exists
if not os.path.exists(INDEX_STORAGE_PATH):
    print(f"Index not found at '{INDEX_STORAGE_PATH}'. Creating new index...")
    print("This process may take a while depending on your internet connection.")

    documents = SimpleDirectoryReader(DOCUMENTS_FOLDER).load_data()
    index = VectorStoreIndex.from_documents(documents, show_progress=True)
    index.storage_context.persist(persist_dir=INDEX_STORAGE_PATH)
    print("Index created and saved successfully!")
else:
    print(f"\nLoading existing index from '{INDEX_STORAGE_PATH}'...")
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_STORAGE_PATH)
    index = load_index_from_storage(storage_context)
    print("Index loaded successfully!")

print("\nAI ready to answer questions. Type 'exit' to quit.")
print("-" * 50)
query_engine = index.as_query_engine(streaming=True)

while True:
    question = input("Your question: ")
    if question.lower() in ["exit", "quit", "sair"]:
        break

    response_stream = query_engine.query(question)

    print("\nAI Response:")
    response_stream.print_response_stream()
    print("\n" + "-" * 50)

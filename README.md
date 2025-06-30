# RAG AI Chat with Gemini

A Retrieval-Augmented Generation (RAG) chatbot powered by Google Gemini API that allows you to ask questions about your document collection.

## Features

- **Document Processing**: Automatically processes text files from a specified directory
- **Vector Search**: Uses Gemini embeddings for semantic document search
- **Streaming Responses**: Real-time AI responses using any Gemini model
- **Persistent Storage**: Saves and loads document indices for faster startup
- **Interactive Chat**: Command-line interface for asking questions

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd rag-ai-chat-api-key
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API key**
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the project root:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

4. **Add your documents**
   - Place your text files in the `transcripts/` directory
   - The system will automatically process all `.txt` files

## Usage

Run the application:
```bash
python main.py
```

The first run will:
1. Process all documents in the `transcripts/` folder
2. Create vector embeddings
3. Save the index for future use

Subsequent runs will load the existing index for faster startup.

## Example Interaction

```
Starting RAG AI Chat with Gemini API...
Loading existing index from './storage_gemini'...
Index loaded successfully!

AI ready to answer questions. Type 'exit' to quit.
--------------------------------------------------
Your question: What is the main topic discussed in the documents?

AI Response:
[Streaming response from the AI based on your documents...]
--------------------------------------------------
```

## Project Structure

```
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env                # API key configuration (create this)
├── transcripts/        # Place your text documents here
└── storage_gemini/     # Generated vector index storage
```

## Requirements

- Python 3.8+
- Google API key with Gemini access
- Internet connection for API calls

## License

This project is open source and available under the MIT License.

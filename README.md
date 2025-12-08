# LLM-Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with LangChain, featuring multilingual support, streaming responses, and vector-based document retrieval.

## Features

- **RAG Architecture**: Combines document retrieval with language model generation for accurate, context-aware responses
- **Streaming Responses**: Real-time output streaming for better user experience
- **Multilingual Support**: Built-in translation capabilities for multiple languages
- **Vector Store Integration**: Uses HuggingFace embeddings for semantic document search
- **Interactive CLI**: Simple command-line interface for chatbot interaction
- **Google Gemini Integration**: Powered by Gemini 2.5 Flash Lite language model

## Project Structure

```
llm-chatbot/
├── src/
│   └── agent/
│       ├── __init__.py
│       ├── __main__.py          # Entry point
│       ├── cli.py               # Command-line interface
│       ├── agent_builder.py     # Agent construction logic
│       ├── model.py             # LLM initialization
│       ├── config.py            # Configuration settings
│       ├── tools.py             # Agent tools (retrieval, etc.)
│       ├── streaming.py         # Response streaming logic
│       ├── translation.py       # Translation utilities
│       └── vectorstore.py       # Vector database management
├── tests/
│   └── test_agent.py            # Unit tests
├── requirements.txt             # Python dependencies
├── pyproject.toml              # Project metadata
├── .env.example                # Environment variables template
└── README.md
```

## Prerequisites

- Python 3.12+
- Google Gemini API key
- HuggingFace token 
- LangSmith API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ChrisDanAsh/LLM-Chatbot.git
cd LLM-Chatbot/llm-chatbot
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Copy the example environment file and add your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
HF_TOKEN=your_huggingface_token_here
LANGSMITH_API_KEY=your_langsmith_key_here
```

**Getting API Keys:**
- **Google Gemini**: https://ai.google.dev/
- **HuggingFace**: https://huggingface.co/settings/tokens
- **LangSmith**: https://smith.langchain.com/

### 5. Install Package (Editable Mode)

```bash
pip install -e .
```

## Usage

### Run the Chatbot

```bash
python -m agent
```

The CLI will start and prompt you for input. Type your questions and press Enter. The chatbot will stream responses in real-time.

**Example interaction:**
```
You: What is retrieval-augmented generation?
Assistant: [streaming response with context from vector store]

You: exit
```

Type `exit`, `quit`, or press `Ctrl+C` to exit.

### Run Tests

```bash
pytest tests/ -v
```

### Code Formatting

The project uses Black and Flake8 for code quality:

```bash
# Format code
black src/ tests/

# Check linting
flake8 src/ tests/
```

## Configuration

Edit `src/agent/config.py` to customize:

- **Chat Model**: Change the LLM (default: `gemini-2.5-flash-lite`)
- **Embedding Model**: Change the embedding model for vector search
- **Vector Store Settings**: Adjust chunk size, overlap, and storage path

## Known Limitations

- **Free Tier Rate Limit**: Google Gemini free tier has a limit of 20 requests/minute
  - Upgrade to a paid tier for production use: https://ai.google.dev/pricing
  - Rate limit errors will show retry messages
  
- **First Run**: Initial execution downloads the embedding model (~90MB), which may take a few minutes

- **Vector Store**: Documents need to be added to the vector store before retrieval works (see `vectorstore.py`)

## Troubleshooting

### Rate Limit Errors

If you see `429 ResourceExhausted` errors:
- Wait a few minutes between requests
- Upgrade your Google API tier
- Monitor usage at: https://ai.dev/usage

## Acknowledgements
- Code based on RAG Tutorial from [https://docs.langchain.com/oss/python/langchain/rag#google-gemini]
- Built with [LangChain](https://github.com/langchain-ai/langchain)
- Powered by [Google Gemini](https://ai.google.dev/)
- Embeddings from [HuggingFace](https://huggingface.co/)

## Contact

- **GitHub**: [@ChrisDanAsh](https://github.com/ChrisDanAsh)
- **Repository**: https://github.com/ChrisDanAsh/LLM-Chatbot
# simple-rag

A simple RAG (Retrieval-Augmented Generation) application built with FastAPI.

## Features

- 🚀 FastAPI-based REST API
- 📦 Modern Python packaging with pyproject.toml
- 🔧 Configuration management with pydantic-settings
- 🌐 CORS support
- 📝 Interactive API documentation (Swagger UI)
- ✅ Health check endpoints

## Prerequisites

- Python 3.9 or higher
- pip or uv package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Junzki/simple-rag.git
cd simple-rag
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install in development mode:
```bash
pip install -e ".[dev]"
```

## Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` file to customize your settings:
- `APP_NAME`: Application name
- `DEBUG`: Enable/disable debug mode
- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `API_V1_PREFIX`: API v1 prefix (default: /api/v1)

## Usage

### Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

Or with custom host and port:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### API Documentation

Once the server is running, you can access:
- Interactive API docs (Swagger UI): http://localhost:8000/docs
- Alternative API docs (ReDoc): http://localhost:8000/redoc
- OpenAPI schema: http://localhost:8000/openapi.json

### Available Endpoints

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint
- `GET /api/v1/` - API v1 root endpoint
- `GET /api/v1/health` - API v1 health check

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
ruff check .
ruff format .
```

## Project Structure

```
simple-rag/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── endpoints.py # API v1 endpoints
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py        # Application configuration
│   ├── models/              # Data models
│   │   └── __init__.py
│   └── services/            # Business logic
│       └── __init__.py
├── tests/                   # Test files
├── .env.example             # Example environment variables
├── .gitignore
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Python dependencies
├── LICENSE
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
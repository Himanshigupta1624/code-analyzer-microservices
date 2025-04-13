# Code Analyzer Microservices

A microservices-based application for analyzing GitHub Pull Requests using AI. The system examines code changes and provides suggestions for improvements related to style, bugs, performance, and best practices.

## Architecture

The application consists of three main components:

1. **FastAPI Frontend** - User-facing API for submitting analysis requests
2. **Django Backend** - Processing service that manages tasks
3. **Celery Worker** - Asynchronous task processor that handles the code analysis

## Setup Instructions

### Prerequisites

- Python 3.8+
- Redis (as message broker)
- GitHub Personal Access Token
- Groq API Key

### Environment Setup

1. Clone the repository:
```
git clone <repository-url>
```
2. Create a virtual environment:
```
python -m venv venv
```
3. Activate the virtual environment:
```
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
4. Install dependencies:
```
pip install -r requirements.txt
```
5. Create a .env file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
### Running the Services

1. Start Redis:
```
# On Windows
redis-server.exe

# Using Docker
docker run -d -p 6379:6379 redis
```
2. Start Django Backend:
```
cd django_project
python manage.py runserver 8001
```
3. Start Celery Worker (in a new terminal):
```
cd django_project
celery -A django_project worker --pool=solo --loglevel=info
```
4. Start FastAPI Frontend (in a new terminal):
```
cd fastapi_app
uvicorn main:app --reload --port 8000
```
### API Usage
#### Analyze a Pull Request
##### Endpoint: POST /start_task/
request
```
{
  "repo_url": "https://github.com/username/repo",
  "pr_number": 1,
  "github_token": "your_github_token"
}
```
response
```
{
  "task_id": "unique-task-id",
  "status": "Task Started"
}
```
#### Check Task Status
##### Endpoint: GET /task_status/{task_id}/
```
{
  "task_id": "unique-task-id",
  "status": "SUCCESS",
  "result": {
    "task_id": "internal-task-id",
    "results": [
      {
        "issues": [
          {
            "type": "style",
            "line": "10",
            "description": "Line too long",
            "suggestion": "Break into multiple lines"
          }
        ]
      }
    ]
  }
}
```
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
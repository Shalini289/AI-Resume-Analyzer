# AI Resume Analyzer Deployment Guide

## Prerequisites

Install:

- Python 3.10+
- pip
- Git
- Gemini API key
- Optional: Docker and Docker Compose

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=sqlite:///resume_analyzer.db
SECRET_KEY=your_secret_key
```

For PostgreSQL:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/resume_analyzer
```

## Install Dependencies

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Install packages:

```bash
pip install -r requirements.txt
```

## Run Streamlit App

```bash
streamlit run app.py
```

Default URL:

```text
http://localhost:8501
```

## Run FastAPI Server

```bash
uvicorn api.main:app --reload
```

Default URL:

```text
http://localhost:8000
```

API docs:

```text
http://localhost:8000/docs
```

## Initialize Database

```bash
python database/init_db.py
```

## Docker Deployment

Build the Docker image:

```bash
docker build -t ai-resume-analyzer .
```

Run the container:

```bash
docker run -p 8501:8501 --env-file .env ai-resume-analyzer
```

## Docker Compose

Run:

```bash
docker-compose up --build
```

Stop:

```bash
docker-compose down
```

## Production Notes

Recommended production setup:

- Use PostgreSQL instead of local SQLite.
- Store `.env` secrets in your hosting provider's secret manager.
- Do not commit `.env`.
- Use a strong `SECRET_KEY`.
- Monitor Gemini API quota and billing limits.
- Use HTTPS in production.
- Keep uploaded files and generated reports outside the app container if persistence is required.

## Deployment Platforms

Possible hosting options:

- Streamlit Community Cloud
- Render
- Railway
- Hugging Face Spaces
- Docker on VPS
- AWS / Azure / GCP

## Streamlit Cloud Deployment

1. Push the project to GitHub.
2. Create a new Streamlit app.
3. Select `app.py` as the entry file.
4. Add secrets in Streamlit settings:

```toml
GEMINI_API_KEY = "your_gemini_api_key"
DATABASE_URL = "sqlite:///resume_analyzer.db"
SECRET_KEY = "your_secret_key"
```

5. Deploy.

## Render Deployment

For Streamlit:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

For FastAPI:

```bash
uvicorn api.main:app --host 0.0.0.0 --port $PORT
```

## Testing Before Deployment

Run:

```bash
python -m pytest -q
```

Expected result:

```text
15 passed
```

## Common Issues

### Gemini Quota Exhausted

Error:

```text
ResourceExhausted: 429 quota exceeded
```

Fix:

- Wait for quota reset.
- Upgrade Gemini plan.
- Reduce repeated AI calls.
- Use Resume Insights, which works without Gemini generation.

### Missing Dependencies

Fix:

```bash
pip install -r requirements.txt
```

### PDF Upload Fails

Check:

- File is a valid PDF.
- `pypdf` is installed.
- File is not encrypted or corrupted.

### Database Connection Fails

Check:

- `DATABASE_URL` is correct.
- PostgreSQL server is running.
- `psycopg2-binary` is installed.

### Streamlit Does Not Start

Try:

```bash
python -m streamlit run app.py
```

## Security Checklist

- `.env` is ignored by Git.
- API keys are not committed.
- JWT `SECRET_KEY` is strong.
- Production database credentials are private.
- Debug logs do not expose secrets.

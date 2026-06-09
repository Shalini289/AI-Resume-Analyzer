# Application

APP_NAME = "AI Resume Analyzer"

VERSION = "1.0.0"

# ATS

MAX_ATS_SCORE = 100

# Resume Processing

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

TOP_K_RESULTS = 4

VECTOR_STORE_PATH = "vector_store"

# Reports

REPORTS_FOLDER = "reports"

# Uploads

UPLOAD_FOLDER = "uploads"

ALLOWED_FILE_TYPES = [
    "pdf"
]

# Gemini

GEMINI_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "models/embedding-001"

# UI

PRIMARY_COLOR = "#1E88E5"

SUCCESS_COLOR = "#4CAF50"

WARNING_COLOR = "#FFC107"

ERROR_COLOR = "#F44336"
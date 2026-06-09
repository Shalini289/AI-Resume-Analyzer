# AI Resume Analyzer API Documentation

Base URL:

```text
http://localhost:8000
```

## Overview

The AI Resume Analyzer API provides endpoints for authentication, resume analysis, interview question generation, and recruiter dashboard data.

## Authentication

### Register User

```http
POST /auth/register
```

Request body:

```json
{
  "name": "Shalini",
  "email": "shalini@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "success": true,
  "user_id": 1
}
```

### Login User

```http
POST /auth/login
```

Request body:

```json
{
  "email": "shalini@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "success": true,
  "token": "jwt_access_token"
}
```

## Resume

### Analyze Resume

```http
POST /resume/analyze
```

Form data:

| Field | Type | Required | Description |
|---|---|---:|---|
| `file` | PDF file | Yes | Resume PDF |
| `jd` | string | Yes | Job description |

Example response:

```json
{
  "ats_score": 80,
  "matching_skills": ["Python", "SQL"],
  "missing_skills": ["Docker"],
  "strengths": ["Strong project experience"],
  "suggestions": ["Add measurable achievements"]
}
```

## Interview

### Generate Interview Questions

```http
POST /interview/generate
```

Request body:

```json
{
  "resume_text": "Candidate resume text...",
  "job_description": "Job description text..."
}
```

Response:

```json
{
  "questions": "Generated interview questions..."
}
```

## Recruiter

### Recruiter Dashboard

```http
GET /recruiter/dashboard
```

Response:

```json
{
  "message": "Recruiter Dashboard"
}
```

### Top Candidates

```http
GET /recruiter/top-candidates
```

Response:

```json
{
  "candidates": [
    {
      "name": "Candidate A",
      "ats_score": 91
    },
    {
      "name": "Candidate B",
      "ats_score": 88
    }
  ]
}
```

## Health Check

### Home

```http
GET /
```

Response:

```json
{
  "message": "AI Resume Analyzer API Running"
}
```

## Error Notes

AI-powered routes may return fallback content if the Gemini API quota is exhausted or temporarily unavailable.

# LedgerLens Architecture

## Project Overview

LedgerLens is an AI-powered document intelligence platform that extracts structured information from invoices and receipts using OpenAI GPT-5.5.

The application follows a modular architecture using FastAPI for the backend, Streamlit for the frontend, and SQLite for data storage.

---

# High-Level Architecture

User
    │
    ▼
Streamlit Frontend
    │
    ▼
FastAPI Backend
    │
    ▼
AI Processing
    │
    ▼
Validation
    │
    ▼
SQLite Database

---

# Project Structure

LedgerLens/
│
├── backend/
├── frontend/
├── uploads/
├── tests/
├── docs/
│
├── README.md
├── ARCHITECTURE.md
├── requirements.txt
└── Dockerfile

---

# Backend Structure

backend/

api/
    API Endpoints

config/
    Application Configuration

database/
    Database Connection

models/
    SQLAlchemy Models

schemas/
    Pydantic Schemas

services/
    Business Logic

utils/
    Helper Functions

---

# Technology Stack

Frontend
- Streamlit

Backend
- FastAPI

Programming Language
- Python 3.13

AI
- OpenAI GPT-5.5

Validation
- Pydantic

Database
- SQLite

Deployment
- Docker
- Google Cloud Run

Monitoring
- Prometheus
- Grafana

---

# Current Development Status

✅ Project Setup

✅ FastAPI

✅ Configuration

✅ API Routing

⬜ Upload Module

⬜ AI Processing

⬜ Database

⬜ Review Queue

⬜ Deployment

---

# Design Principles

- Modular architecture
- Separation of concerns
- Environment-based configuration
- RESTful API design
- Scalable project structure

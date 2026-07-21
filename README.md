# 📄 LedgerLens

> **AI-Powered Invoice Processing System** built using **FastAPI, Streamlit, SQLAlchemy, SQLite, Docker, and Google Gemini AI**.

LedgerLens is an intelligent invoice management system that automates invoice processing using Artificial Intelligence. Users can upload invoices, extract key information using Gemini AI, review extracted data, approve or reject invoices, visualize analytics, and export results.

---

## 🚀 Features

### 📥 Invoice Management
- Upload invoice (Image/PDF)
- Invoice preview
- Store invoices securely
- Invoice history

### 🤖 AI Processing
- Google Gemini AI integration
- Automatic invoice data extraction
- Vendor detection
- Invoice number detection
- GST number extraction
- Invoice date extraction
- Amount & tax extraction
- AI confidence tracking

### ✅ Human Review Workflow
- Process invoice using AI
- Approve invoice
- Reject invoice
- Review status tracking
- Smart action buttons

### 📊 Dashboard
- KPI cards
- Financial analytics
- Invoice statistics
- AI processing status
- Review status
- Progress tracking
- Interactive Plotly charts

### 🔍 Search & Filters
- Search by filename
- Search by vendor
- Search by invoice number
- Filter by AI status
- Filter by review status

### 📤 Export
- Download invoice data as CSV

---

# 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| AI | Google Gemini |
| Charts | Plotly |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
LedgerLens
│
├── backend
│   ├── api
│   ├── models
│   ├── services
│   ├── database.py
│   ├── config.py
│   └── main.py
│
├── frontend
│   ├── components
│   ├── utils
│   └── app.py
│
├── docs
├── scripts
├── tests
├── uploads
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
└── LICENSE
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <repository-url>
```

```bash
cd LedgerLens
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create a `.env` file.

Example

```text
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-3.5-flash-lite
DATABASE_URL=sqlite:///ledgerlens.db
```

---

## Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 🖥️ Dashboard

The dashboard provides:

- Total invoices
- AI completed
- Pending review
- Approved invoices
- Rejected invoices
- Financial analytics
- Progress tracking
- Interactive charts
- Vendor analytics
- Recent activity

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload invoice |
| GET | `/uploads` | Get invoice history |
| POST | `/process/{id}` | Process invoice with AI |
| POST | `/review/{id}/approve` | Approve invoice |
| POST | `/review/{id}/reject` | Reject invoice |

---

# 🧪 Testing

Run tests using:

```bash
pytest
```

---

# 🐳 Docker

Build image

```bash
docker build -t ledgerlens .
```

Run container

```bash
docker-compose up
```

---

# 📈 Future Improvements

- Multi-user authentication
- Role-based access control
- OCR engine integration
- Cloud database support
- Email notifications
- Audit logs
- REST API documentation
- Deployment on AWS/Azure

---

# 👨‍💻 Author

**Amandeep kaur**

AI Enthusiast | Python Developer | FastAPI | Streamlit

---

# 📄 License

This project is licensed under the MIT License.
# Masar

AI-powered project management intelligence platform designed to analyze software projects and recommend the most suitable development methodology using artificial intelligence.

Masar combines a modern responsive frontend with a FastAPI backend and Gemini AI integration to deliver smart project analysis, risk evaluation, and team recommendations for software development projects.

---

## Overview

Masar helps developers, students, and project teams make better project management decisions by analyzing project requirements and generating AI-powered recommendations.

The platform evaluates project complexity, scalability, collaboration requirements, and technical uncertainty to determine the optimal project management methodology.

---

## Core Features

### AI Methodology Analyzer

Analyze software projects using AI and receive recommendations for the most suitable project management methodology such as Agile, Scrum, Kanban, or Waterfall.

### Smart Risk Assessment

Automatically identifies project complexity and potential development risks.

### Recommended Team Structure

Suggests the ideal team composition based on project scale and technical requirements.

### EVM Calculator

Integrated Earned Value Management calculator for project performance tracking.

### Modern Responsive Interface

Clean and responsive user interface designed for accessibility and usability.

### FastAPI Backend

High-performance backend architecture built with FastAPI and Python.

### Gemini AI Integration

Powered by Google Gemini AI for intelligent project analysis and recommendation generation.

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* Uvicorn

### AI & APIs

* Gemini API
* Google Generative AI

---

## How It Works

1. The user enters a software project description.
2. The backend sends the project data to Gemini AI.
3. The AI analyzes:

   * Project complexity
   * Collaboration requirements
   * Risk level
   * Scalability concerns
   * Development uncertainty
4. Masar returns:

   * Recommended methodology
   * Risk level
   * Suggested team structure
   * AI-generated explanation

---

## Project Structure

```text
Masar/
│
├── front-end/
│   ├── index.html
│   ├── methodology_analyzer.html
│   ├── evm-calculator.html
│   └── style.css
│
├── back-end/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── README.md
└── .gitignore
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/masar.git
```

---

### 2. Backend Setup

Navigate to the backend folder:

```bash
cd back-end
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the backend server:

```bash
uvicorn app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### 3. Frontend Setup

Run a local server from the project root:

```bash
py -m http.server 8001
```

Open:

```text
http://localhost:8001/front-end/methodology_analyzer.html
```

---

## Future Improvements

* User authentication system
* Dashboard analytics
* Project history tracking
* AI-generated sprint planning
* Team collaboration features
* Deployment to cloud platforms
* Database integration

---

## Developed By

**Shrowq Alharbi**

Designed and developed as an AI-powered project management platform.
